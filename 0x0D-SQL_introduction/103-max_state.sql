-- displays the max temperature of each state
-- of the database hbtn_0c_0 in MySQL server
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
