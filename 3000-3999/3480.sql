SELECT *
FROM (
  VALUES
    (1, 7,  8),
    (2, 11, 12),
    (2, 14, 15),
    (3, 21, 22),
    (4, 28, 29)
) AS t(queue, "left", "right");
