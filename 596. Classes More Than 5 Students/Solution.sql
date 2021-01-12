# Write your MySQL query statement below
SELECT class
FROM
(SELECT COUNT(DISTINCT student) AS nums, class
FROM courses
GROUP BY class) AS example
WHERE nums >= 5;