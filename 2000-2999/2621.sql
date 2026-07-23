select products.name from products,providers where 
products.id_providers=providers.id and
 amount between 10 and 20 and providers.name like 'P%';
