use largedataset;

show tables;

desc customers;

-- get the order id, order date and customer names when the ordder is placed

select orders.OrderID, orders.OrderDate, customers.CustomerID,customers.CustomerName from orders
INNER join customers on orders.CustomerID= customers.CustomerID limit 5;

-- Join three tables
select orders.OrderID, customers.CustomerName,shippers.ShipperName from ((orders
INNER join customers on orders.CustomerID= customers.CustomerID)
inner join shippers on orders.ShipperID = shippers.ShipperID) limit 5;

-- left joint
-- get all the customers with their order id 
select customers.CustomerName, orders.OrderID from customers
right join orders
on customers.CustomerID = orders.CustomerID;

-- Outer joims aand unions
select City from customers
union all
select City from suppliers order by City;
