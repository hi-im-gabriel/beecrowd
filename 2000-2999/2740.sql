SELECT Concat('Podium: ', team) as name
FROM League
WHERE position IN (SELECT MIN(position) FROM League)
UNION ALL
SELECT Concat('Podium: ', team) 
FROM League
WHERE position IN (SELECT MIN(position)+1 FROM League)
UNION ALL
SELECT Concat('Podium: ', team) 
FROM League
WHERE position IN (SELECT MIN(position)+2 FROM League)
UNION ALL
SELECT Concat('Demoted: ', team) 
FROM League
WHERE position IN (SELECT MAX(position)-1 FROM League)
UNION ALL
SELECT Concat('Demoted: ', team) 
FROM League
WHERE position IN (SELECT MAX(position) FROM League)
