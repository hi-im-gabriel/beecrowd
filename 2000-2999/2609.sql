select categories.name, SUM(products.amount) from products join categories on products.id_categories = categories.id group by categories.name;
