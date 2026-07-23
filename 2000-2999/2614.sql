SELECT c.name, r.rentals_date
FROM customers AS c
JOIN rentals AS r ON c.id = r.id_customers
WHERE extract(month FROM r.rentals_date) = 9;
