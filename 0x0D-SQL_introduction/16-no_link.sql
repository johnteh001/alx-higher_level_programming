-- script that list all records of table
-- do not list rows without value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
