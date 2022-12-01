-- Lists all cities of California in the database
SELECT id, name FROM cities  WHERE state_id = 1 ORDER BY cities.id;
