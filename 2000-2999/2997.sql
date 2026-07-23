WITH salarios AS (
    SELECT ev.matr, SUM(v.valor) AS bruto
    FROM emp_venc ev
    JOIN vencimento v ON v.cod_venc = ev.cod_venc
    GROUP BY ev.matr
), descontos AS (
    SELECT ed.matr, SUM(d.valor) AS total
    FROM emp_desc ed
    JOIN desconto d ON d.cod_desc = ed.cod_desc
    GROUP BY ed.matr
)
SELECT dep.nome AS "Departamento",
       e.nome AS "Empregado",
       ROUND(COALESCE(s.bruto, 0), 2) AS "Salario Bruto",
       ROUND(COALESCE(ds.total, 0), 2) AS "Total Desconto",
       ROUND(COALESCE(s.bruto, 0) - COALESCE(ds.total, 0), 2) AS "Salario Liquido"
FROM empregado e
JOIN divisao div ON div.cod_divisao = e.lotacao_div
JOIN departamento dep ON dep.cod_dep = div.cod_dep
LEFT JOIN salarios s ON s.matr = e.matr
LEFT JOIN descontos ds ON ds.matr = e.matr
ORDER BY COALESCE(s.bruto, 0) - COALESCE(ds.total, 0) DESC;
