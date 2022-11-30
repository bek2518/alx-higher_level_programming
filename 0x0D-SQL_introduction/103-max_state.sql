-- Displays top 3 cities temp during July and August
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state DESC;
