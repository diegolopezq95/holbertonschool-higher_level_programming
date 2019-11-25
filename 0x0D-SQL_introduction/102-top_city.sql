-- displays the top 3 cities temperature during July an August
-- by city ordered by temperature (descending)
-- of the database hbtn_0c_0 in MySQL server
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE MONTH = 7 OR MONTH = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
