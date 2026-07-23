SELECT c.id, c.name
FROM customers AS c
WHERE c.id NOT IN(
    SELECT l.id_customers
    FROM locations AS l
    WHERE l.id_customers = c.id);
