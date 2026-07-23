SELECT pd.name, pv.name, pd.price
FROM products AS pd
JOIN providers AS pv ON pv.id = pd.id_providers
JOIN categories AS c ON c.id = pd.id_categories
WHERE pd.price > 1000 AND c.name LIKE 'Super Luxury';
