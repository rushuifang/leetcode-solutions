# Write your MySQL query statement below
SELECT Email
FROM
    (SELECT COUNT(Email) AS Num, Email
    FROM Person
    GROUP BY Email) AS Statistics
WHERE Num > 1