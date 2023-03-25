# Write your MySQL query statement below
select employee_id, CASE WHEN employee_id%2 = 1 and name not like 'm%' THEN salary ELSE 0 END AS bonus from Employees order by employee_id asc;