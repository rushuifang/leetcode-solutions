# Write your MySQL query statement below
SELECT Customers
FROM
    (SELECT Customers.Name AS Customers, Orders.Id AS Id
    FROM Customers LEFT JOIN
    Orders
    ON Customers.Id = Orders.CustomerId)
    AS newTable
WHERE Id IS NULL

-- another solution
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);