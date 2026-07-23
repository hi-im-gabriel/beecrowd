SELECT temperature, COUNT(*) AS number_of_records FROM (
  SELECT records.*, row_number() OVER (PARTITION BY temperature)
  - row_number() OVER (PARTITION BY temperature, mark) AS seq 
        FROM records) t
GROUP BY temperature, mark, seq ORDER BY mark;
