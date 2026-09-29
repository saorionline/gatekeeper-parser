# 🤖 Gatekeeper Parser · Fase Gama

Proyecto colaborativo para aprender a programar robots mediante **agentes de IA**: cada participante construye su propio agente, el grupo lo revisa junto a un mentor certificado y el resultado se sustenta en un foro abierto.

Este repositorio contiene el material de la **Fase Gama, Día 1 (Rol 4: Ingesta y validación)**. Aquí, un robot revisor en Python lee datos bancarios escritos en Markdown, los valida con reglas y consultas SQL, y genera un reporte automático.

---

## 🎯 Misión

Divulgar y promover la programación de robots mediante agentes de IA **creados por cada aprendiz** y **revisados en grupo** por alguien certificado. Cada solución se sustenta públicamente en el foro:

> ### 📖 Aprender en red (foro de sustentación)
> **¡El conocimiento se expande cuando lo compartimos!**
>
> Entra al foro de la lección para ver las respuestas, la estructura de carpetas y las soluciones de tus compañeros. Analiza cómo resolvieron cada integración, compara sus enfoques y encuentra nuevas formas de mejorar tus soluciones con lo que los demás sustentaron.

## 🔭 Visión

Tejer una red de colaboradores con un perfil técnico común, que sirve de base para todas las cápsulas de aprendizaje:

| Área | Cómo se aprovecha |
|---|---|
| 🐍 **Python** | Todos lo conocen, así que es el lenguaje base de todas las cápsulas. |
| ⚙️ **Ingeniería** | Entienden sistemas, restricciones y validación. Se espera que **justifiquen sus decisiones**, no solo que entreguen un resultado. |
| 🧠 **IA y agentes** | Los roles están escritos como agentes. Cada aprendiz puede "hacer de agente" y seguir las reglas de su archivo de rol. |
| 🔁 **Automatización** | Cada ejercicio termina en algo **ejecutable y repetible**, no en una respuesta escrita a mano. |
| 🗃️ **Bases de datos / SQL** | El proyecto de divisas es, por naturaleza, de base de datos: cuentas, libro mayor y tasas. |

---

## 🧭 Metodología de trabajo

### 1. Acceso, infraestructura y entorno

| Aspecto | Especificación |
|---|---|
| **Comunicación** | El seguimiento técnico y las notificaciones se hacen por mensaje privado en un servidor dedicado de **Discord**. |
| **Insumos** | Los ejercicios se distribuyen como archivos dentro de este repositorio (`git clone `) en **Visual Studio Code* o tu editor de código preferido. |
| **Entorno** | Se usa principalmente **Visual Studio Code**. Google Colab no permite importar módulos secundarios ni archivos de soporte sin configurar celdas adicionales. |
| **Entrega** | `gama.ipynb` y `reporte.md` se suben a una carpeta personal de **Entregas** en Google Drive, con permisos independientes para cada estudiante. |

### 2. Fases y dedicación

| Fase | Dedicación | Enfoque |
|---|---|---|
| **Gama** | 20 min/día | Bases de datos y automatizaciones básicas para agentes de IA. |
| **Beta → Delta → Sigma** | Según la dedicación semanal | Progresión escalonada con mayor complejidad. |

> La fase inicial se elige con flexibilidad y se puede cambiar más adelante.

### 3. Tarea práctica: Día 1 · Ingesta y validación (Rol 4)

- **Objetivo:** ejecutar scripts de Python que leen y validan los datos de archivos Markdown (`extracto_banco.md` y `rates.md`).
- **Verificaciones:** detectar inconsistencias, validar monedas, fechas y valores numéricos, y encontrar registros duplicados.
- **Criterio de aprobación:** notificar por mensaje privado en Discord y pasar la revisión técnica. Al aprobar, se entrega la acreditación (**pin animado**) que da acceso a la siguiente etapa interactiva.

---

## 📂 Estructura del repositorio

| Archivo | Formato | Rol |
|---|---|---|
| [`gama.ipynb`](gama.ipynb) | Jupyter Notebook | Guía paso a paso: leer, encender el robot y resolver las misiones. |
| [`revisar.py`](revisar.py) | 🐍 Python | El **robot revisor**: contiene las reglas de validación. |
| [`buscar_repetidos.sql`](buscar_repetidos.sql) | 🗃️ SQL | Consulta que busca referencias duplicadas en el extracto. |
| [`extracto_banco.md`](extracto_banco.md) | 📝 Markdown | Datos de entrada: movimientos bancarios. |
| [`rates.md`](rates.md) | 📝 Markdown | Datos de entrada: tasas de cambio. |
| `reporte.md` | 🧾 Markdown | **Salida** que genera el robot (no viene incluida; se crea al ejecutarlo). |

```text
extracto_banco.md ─┐
                   ├──► revisar.py ──(SQLite + buscar_repetidos.sql)──► reporte.md
rates.md ──────────┘
```

El robot **solo lee** los archivos de datos y nunca los modifica. Cada fila del reporte queda marcada como:

- ✅ **VÁLIDO**: no tiene problemas.
- ❌ **RECHAZADO**: tiene errores de formato, moneda, fecha o duplicados.
- 🚨 **SOSPECHOSO**: la descripción contiene instrucciones o palabras de alerta.

### Reglas que aplica el robot

- **Monedas conocidas:** `USD`, `EUR`, `COP`, `JPY`, `BRL`, cada una con sus decimales permitidos (`JPY` no admite decimales).
- **Monedas pausadas:** `BRL` está en estado *HALTED* y no se puede usar.
- **Fechas:** deben existir en el calendario (por ejemplo, `2026-09-31` no existe).
- **Montos:** deben ser números válidos y respetar los decimales de su moneda.
- **Duplicados:** se detectan con SQL (`GROUP BY` + `HAVING`).
- **Tasas:** deben indicar su fuente (`source`) y tener una fecha válida.

---

## 🚀 Cómo empezar

**Requisitos:** Python 3.9 o superior (solo usa la biblioteca estándar: `sqlite3`, `decimal`, `datetime` y `pathlib`) y VS Code con la extensión de Jupyter.

1. Clona el repositorio  en una carpeta local.
2. Ábrela en VS Code y abre `gama.ipynb`.
3. Ejecuta las celdas en orden con **Shift + Enter**.
4. También puedes ejecutar el robot directamente desde la terminal:

   ```bash
   python revisar.py
   ```

5. Revisa el `reporte.md` generado.

## 🛠️ Misiones

El robot viene **incompleto a propósito**. Busca los marcadores `✏️ MISIÓN` en el código:

| Misión | Archivo | Qué hay que hacer |
|---|---|---|
| **1** | `buscar_repetidos.sql` | Ajustar la condición `HAVING` para que solo marque como repetido lo que de verdad lo es. |
| **2** | `revisar.py` | Llenar `PALABRAS_SOSPECHOSAS` para que el robot detecte descripciones que dan órdenes. |

Cuando termines, ejecuta de nuevo el robot, compara el reporte y **justifica tus decisiones** en el foro de sustentación.

## 📬 Entrega

1. Sube `gama.ipynb` (con tus respuestas) y `reporte.md` a tu carpeta personal de **Entregas** en Google Drive.
2. Avisa por mensaje privado en **Discord**.
3. Espera la revisión técnica y recibe tu 🏅 **pin animado** para pasar a la siguiente etapa.

## 🤝 Convivencia

Antes de colaborar, lee el [Código de conducta](CODIGO_CONDUCTA.MD).
