SELECT m.id, m.name
FROM movies as m, genres as g
WHERE m.id_genres=g.id AND g.description='Action';
