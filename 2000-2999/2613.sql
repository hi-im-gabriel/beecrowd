select movies.id, movies.name
from movies, prices
where movies.id_prices = prices.id
and prices.value < 2;
