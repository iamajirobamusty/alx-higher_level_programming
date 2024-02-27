-- output all values with a name column
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC
WHERE `name` IS NOT NULL;
