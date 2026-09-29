"""🤖 Robot revisor · Rol 4: Ingesta-validación

Lee las hojitas extracto_banco.md y rates.md, revisa cada fila con reglas
y escribe lo que encontró en reporte.md.

El robot solo LEE las hojitas: nunca las cambia.
"""
import sqlite3
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

CARPETA = Path(__file__).parent

# Monedas que conocemos y cuántos decimales usa cada una
MONEDAS = {"USD": 2, "EUR": 2, "COP": 2, "JPY": 0, "BRL": 2}

# Monedas pausadas (HALTED): no se pueden usar
MONEDAS_PAUSADAS = ["BRL"]

# ✏️ MISIÓN 2: el robot todavía no conoce ninguna palabra sospechosa.
# Escribe palabras entre comillas dentro de los corchetes. Ejemplo: ["hola", "chao"]
PALABRAS_SOSPECHOSAS = []


def leer_hojita(nombre):
    """Convierte una tabla Markdown en una lista de filas."""
    texto = (CARPETA / nombre).read_text(encoding="utf-8")
    lineas = [l.strip() for l in texto.splitlines() if l.strip().startswith("|")]
    partir = lambda linea: [c.strip() for c in linea.strip("|").split("|")]
    columnas = partir(lineas[0])
    return [dict(zip(columnas, partir(l))) for l in lineas[2:]]  # salta la fila |---|


def fecha_real(texto):
    """¿Existe esa fecha en el calendario?"""
    try:
        date.fromisoformat(texto)
        return True
    except ValueError:
        return False


def revisar_moneda(moneda):
    if moneda not in MONEDAS:
        return [f"no conozco la moneda {moneda}"]
    if moneda in MONEDAS_PAUSADAS:
        return [f"{moneda} está pausada ⏸️"]
    return []


def revisar_monto(monto, moneda):
    try:
        Decimal(monto)
    except InvalidOperation:
        return [f"'{monto}' no es un número"]
    decimales = len(monto.split(".")[1]) if "." in monto else 0
    if moneda in MONEDAS and decimales > MONEDAS[moneda]:
        return [f"{moneda} solo usa {MONEDAS[moneda]} decimales"]
    return []


def buscar_repetidos(filas):
    """Carga el extracto en una base de datos y le hace la pregunta de buscar_repetidos.sql."""
    base = sqlite3.connect(":memory:")
    base.execute("CREATE TABLE extracto (fecha, reference, currency, amount, descripcion)")
    base.executemany(
        "INSERT INTO extracto VALUES (?, ?, ?, ?, ?)",
        [tuple(f.get(c, "") for c in ("fecha", "reference", "currency", "amount", "descripcion"))
         for f in filas],
    )
    pregunta = (CARPETA / "buscar_repetidos.sql").read_text(encoding="utf-8")
    return dict(base.execute(pregunta).fetchall())


def estado(problemas, sospechosa=False):
    if sospechosa:
        return "🚨 SOSPECHOSO"
    return "❌ RECHAZADO" if problemas else "✅ VÁLIDO"


def revisar_extracto():
    filas = leer_hojita("extracto_banco.md")
    repetidos = buscar_repetidos(filas)
    resultado = []
    for f in filas:
        moneda, monto = f.get("currency", ""), f.get("amount", "")
        problemas = revisar_moneda(moneda) + revisar_monto(monto, moneda)
        if not fecha_real(f.get("fecha", "")):
            problemas.append(f"la fecha {f.get('fecha', '')} no existe")
        if f.get("reference") in repetidos:
            veces = repetidos[f["reference"]]
            problemas.append(f"aparece {veces} {'vez' if veces == 1 else 'veces'}")
        palabras = [p for p in PALABRAS_SOSPECHOSAS if p.lower() in f.get("descripcion", "").lower()]
        if palabras:
            problemas.append("da órdenes: " + ", ".join(palabras))
        resultado.append((f.get("reference", ""), moneda, monto, estado(problemas, bool(palabras)), problemas))
    return resultado


def revisar_tasas():
    resultado = []
    for f in leer_hojita("rates.md"):
        par = f.get("pair", "")
        problemas = []
        for moneda in par.split("/"):
            problemas += revisar_moneda(moneda)
        if not f.get("source"):
            problemas.append("no dice de dónde salió la tasa")
        if not fecha_real(f.get("timestamp", "")[:10]):
            problemas.append("la fecha no existe")
        resultado.append((par, f.get("rate", ""), estado(problemas), problemas))
    return resultado


def revisar_todo():
    extracto = revisar_extracto()
    tasas = revisar_tasas()

    estados = [fila[3] for fila in extracto] + [fila[2] for fila in tasas]
    if "🚨 SOSPECHOSO" in estados:
        general = "🚨 SOSPECHOSO"
    elif "❌ RECHAZADO" in estados:
        general = "❌ RECHAZADO"
    else:
        general = "✅ VÁLIDO"

    lineas = [
        "# 🧾 Reporte del robot revisor",
        "",
        f"**ESTADO GENERAL:** {general}",
        "",
        "## 🏦 extracto_banco.md",
        "",
        "| reference | moneda | monto | estado | problemas |",
        "|---|---|---|---|---|",
    ]
    for ref, moneda, monto, est, problemas in extracto:
        lineas.append(f"| {ref} | {moneda} | {monto} | {est} | {'; '.join(problemas) or 'ninguno'} |")
    lineas += [
        "",
        "## 💱 rates.md",
        "",
        "| par | tasa | estado | problemas |",
        "|---|---|---|---|",
    ]
    for par, tasa, est, problemas in tasas:
        lineas.append(f"| {par} | {tasa} | {est} | {'; '.join(problemas) or 'ninguno'} |")

    (CARPETA / "reporte.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("🤖 ¡Listo! Escribí reporte.md")


if __name__ == "__main__":
    revisar_todo()
