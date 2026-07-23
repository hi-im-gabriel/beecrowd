WITH media AS (
SELECT sub2.departamento, 
        sub2.divisao,
        ROUND(AVG(valor_salario),2) media
    FROM ( 
        SELECT sub1.empregado,  
               sub1.departamento, 
               sub1.divisao,
               SUM(sub1.valor_vencimento) - SUM(sub1.valor_desconto) valor_salario
        FROM (
            SELECT emp.nome empregado,
                   dep.nome departamento,
                   div.nome divisao,
                   SUM(venc.valor) valor_vencimento,
                   0 valor_desconto
            FROM departamento dep
            INNER JOIN divisao     div ON div.cod_dep     = dep.cod_dep
            INNER JOIN empregado   emp ON emp.lotacao_div = div.cod_divisao
            INNER JOIN emp_venc   empv ON empv.matr       = emp.matr
            INNER JOIN vencimento venc ON venc.cod_venc   = empv.cod_venc
            GROUP BY emp.nome,
                   dep.nome,
                   div.nome

            UNION ALL

            SELECT emp.nome empregado,
                   dep.nome departamento,
                   div.nome divisao,
                   0 valor_vencimento,
                   SUM(des.valor) valor_desconto
            FROM departamento dep
            INNER JOIN divisao     div ON div.cod_dep     = dep.cod_dep
            INNER JOIN empregado   emp ON emp.lotacao_div = div.cod_divisao
            INNER JOIN emp_desc   empd ON empd.matr       = emp.matr
            INNER JOIN desconto    des ON des.cod_desc    = empd.cod_desc
            GROUP BY emp.nome,
                   dep.nome,
                   div.nome
        ) sub1

        GROUP BY sub1.empregado,  
               sub1.departamento, 
               sub1.divisao
        ORDER BY sub1.departamento, 
                 sub1.divisao

    ) sub2
    GROUP BY sub2.departamento, 
           sub2.divisao
)
SELECT departamento, divisao, MAX(media) media 
FROM media med1
GROUP BY departamento, divisao
HAVING MAX(media) = (SELECT MAX(media) FROM media med WHERE med.departamento =  med1.departamento)
ORDER BY 3 DESC;
