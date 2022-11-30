-- Displays top 3 cities temp during July and August
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
