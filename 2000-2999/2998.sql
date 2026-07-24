WITH monthly_operations AS (
    SELECT client_id, month, SUM(profit) AS profit
    FROM operations
    GROUP BY client_id, month
), accumulated_operations AS (
    SELECT
        c.name,
        c.investment,
        mo.month,
        SUM(mo.profit) OVER (
            PARTITION BY c.id
            ORDER BY mo.month
        ) AS accumulated
    FROM clients c
    JOIN monthly_operations mo ON mo.client_id = c.id
), paybacks AS (
    SELECT
        name,
        investment,
        month,
        accumulated - investment AS return,
        ROW_NUMBER() OVER (
            PARTITION BY name, investment
            ORDER BY month
        ) AS position
    FROM accumulated_operations
    WHERE accumulated >= investment
)
SELECT
    name,
    investment,
    month AS month_of_payback,
    return
FROM paybacks
WHERE position = 1
ORDER BY return DESC;
