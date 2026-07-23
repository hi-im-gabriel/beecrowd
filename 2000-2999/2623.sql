select products.name, categories.name from products,categories where 
products.id_categories IN (1,2,3,6,9)
and products.amount>100
and products.id_categories=categories.id 
order by products.id_categories;
