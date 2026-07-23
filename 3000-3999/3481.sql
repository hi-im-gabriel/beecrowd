SELECT *
FROM (
  VALUES
    (1,  'LEAF'),
    (15, 'INNER'),
    (20, 'LEAF'),
    (30, 'INNER'),
    (32, 'LEAF'),
    (35, 'INNER'),
    (40, 'LEAF'),
    (50, 'ROOT'),
    (55, 'LEAF'),
    (60, 'INNER'),
    (70, 'LEAF'),
    (75, 'INNER'),
    (80, 'LEAF'),
    (90, 'INNER'),
    (95, 'LEAF')
) AS t(node_id, type);
