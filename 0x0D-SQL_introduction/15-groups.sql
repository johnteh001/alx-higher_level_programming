-- script lists the number of records with same score
-- result shows the score and the number or records 
SELECT score, COUNT(score) number FROM second_table
GROUP BY score
ORDER BY number DESC;
