# Write your MySQL query statement below
select name from Customer where referee_id IS null or referee_id not in (2);