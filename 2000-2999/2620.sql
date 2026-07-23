select customers.name,orders.id from
customers,orders where 
orders.orders_date>='2016-01-01' and 
orders.orders_date<='2016-06-30' and 
customers.id=orders.id_customers;
