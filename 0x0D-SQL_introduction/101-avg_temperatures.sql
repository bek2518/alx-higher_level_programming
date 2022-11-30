-- Displays average temprature by city
.import tempratures.sql hbtn_0c_0

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;