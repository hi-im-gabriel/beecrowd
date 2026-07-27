WITH salarios AS (
    SELECT
        e.matr,
        e.nome,
        e.lotacao_div,
        COALESCE((
            SELECT SUM(v.valor)
            FROM emp_venc ev
            JOIN vencimento v ON v.cod_venc = ev.cod_venc
            WHERE ev.matr = e.matr
        ), 0) - COALESCE((
            SELECT SUM(d.valor)
            FROM emp_desc ed
            JOIN desconto d ON d.cod_desc = ed.cod_desc
            WHERE ed.matr = e.matr
        ), 0) AS salario
    FROM empregado e
), medias AS (
    SELECT lotacao_div, AVG(salario) AS media
    FROM salarios
    GROUP BY lotacao_div
)
SELECT
    s.nome,
    ROUND(s.salario, 2) AS salario
FROM salarios s
JOIN medias m ON m.lotacao_div = s.lotacao_div
WHERE s.salario > m.media
  AND s.salario >= 8000.00
ORDER BY s.lotacao_div;
