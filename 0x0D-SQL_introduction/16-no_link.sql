-- lists all records of the table second_table with a name value, by descending score
-- format: score name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
