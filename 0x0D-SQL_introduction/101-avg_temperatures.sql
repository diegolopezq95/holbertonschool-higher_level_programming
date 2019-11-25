-- displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
-- of the database hbtn_0c_0 in MySQL server
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
