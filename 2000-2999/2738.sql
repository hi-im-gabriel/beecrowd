SELECT Candidate.name,ROUND(((Score.math*2) + (specific*3) + (project_plan*5))/10,2)  as avg
FROM Candidate
INNER JOIN Score
ON Candidate.id = Score.candidate_id
ORDER BY avg DESC
