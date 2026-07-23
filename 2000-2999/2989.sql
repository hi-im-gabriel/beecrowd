WITH proventos AS (
    SELECT ev.matr, SUM(v.valor) AS total
    FROM emp_venc ev
    JOIN vencimento v ON v.cod_venc = ev.cod_venc
    GROUP BY ev.matr
), descontos AS (
    SELECT ed.matr, SUM(d.valor) AS total
    FROM emp_desc ed
    JOIN desconto d ON d.cod_desc = ed.cod_desc
    GROUP BY ed.matr
), salarios AS (
    SELECT e.lotacao_div,
           COALESCE(p.total, 0) - COALESCE(ds.total, 0) AS salario
    FROM empregado e
    LEFT JOIN proventos p ON p.matr = e.matr
    LEFT JOIN descontos ds ON ds.matr = e.matr
)
SELECT dep.nome AS departamento,
       div.nome AS divisao,
       ROUND(AVG(s.salario), 2) AS media,
       ROUND(MAX(s.salario), 2) AS maior
FROM departamento dep
JOIN divisao div ON div.cod_dep = dep.cod_dep
JOIN salarios s ON s.lotacao_div = div.cod_divisao
GROUP BY dep.cod_dep, dep.nome, div.cod_divisao, div.nome
ORDER BY AVG(s.salario) DESC;
