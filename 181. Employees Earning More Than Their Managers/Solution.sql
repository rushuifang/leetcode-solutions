# Write your MySQL query statement below
SELECT a.Name AS 'Employee'
FROM Employee As a, Employee As b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary