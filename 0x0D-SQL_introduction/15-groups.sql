-- Lists the number of records with the same score
SELECT score, COUNT(*) AS NUMBER from second_table GROUP BY score ORDER BY number DESC;
