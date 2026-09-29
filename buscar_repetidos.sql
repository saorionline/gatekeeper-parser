-- 🗃️ Buscar filas repetidas en el extracto del banco
-- La tabla "extracto" tiene las mismas columnas que extracto_banco.md.
-- GROUP BY junta las filas que tienen la misma referencia.
-- COUNT(*) cuenta cuántas filas hay en cada grupo.

SELECT reference, COUNT(*) AS veces
FROM extracto
GROUP BY reference
-- ✏️ MISIÓN 1: ¿cuántas veces tiene que aparecer algo para estar REPETIDO?
HAVING COUNT(*) >= 1;
