-- Displays the average temp (fahrenheit) by city
-- Ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
