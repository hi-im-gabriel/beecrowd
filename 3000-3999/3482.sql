SELECT *
FROM (
  VALUES
    ('Francisco', 'Laura'),
    ('Brenda',    'Miguel'),
    ('Laura',     'Miguel'),
    ('Alice',     'Helena')
) AS t(u1_name, u2_name);
