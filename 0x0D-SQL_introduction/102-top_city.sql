-- Displays top 3 cities temp during July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city WHERE month = 'July' OR month = 'August' ORDER BY avg_temp DESC LIMIT 3;
