WITH salarios AS (
    SELECT
        e.matr,
        e.lotacao,
        COALESCE(v.total_vencimentos, 0) - COALESCE(d.total_descontos, 0) AS salario
    FROM empregado e
    LEFT JOIN (
        SELECT ev.matr, SUM(v.valor) AS total_vencimentos
        FROM emp_venc ev
        JOIN vencimento v ON v.cod_venc = ev.cod_venc
        GROUP BY ev.matr
    ) v ON v.matr = e.matr
    LEFT JOIN (
        SELECT ed.matr, SUM(d.valor) AS total_descontos
        FROM emp_desc ed
        JOIN desconto d ON d.cod_desc = ed.cod_desc
        GROUP BY ed.matr
    ) d ON d.matr = e.matr
)
SELECT
    dep.nome AS "Nome Departamento",
    COUNT(s.matr) AS "Numero de Empregados",
    COALESCE(ROUND(AVG(s.salario), 2), 0) AS "Media Salarial",
    COALESCE(MAX(s.salario), 0) AS "Maior Salario",
    COALESCE(MIN(s.salario), 0) AS "Menor Salario"
FROM departamento dep
LEFT JOIN salarios s ON s.lotacao = dep.cod_dep
GROUP BY dep.cod_dep, dep.nome
ORDER BY "Media Salarial" DESC;
