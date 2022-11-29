-- Displays the max temp of each state
-- Ordered state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
