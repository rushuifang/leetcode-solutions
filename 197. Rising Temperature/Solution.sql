# Write your MySQL query statement below
SELECT 
    Weather.id
FROM 
    Weather
JOIN
    Weather AS w ON DATEDIFF(Weather.recordDate, w.recordDate) = 1
AND
    Weather.temperature > w.temperature
;