-- Write your PostgreSQL query statement below
select  
  d.name AS "Department",
  e.name AS "Employee",
  e.salary AS "Salary"
FROM (
    select e.name,e.salary, e.departmentId,
  DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rank
  FROM Employee e
) e
join Department as d
 on e.departmentId = d.id
where e.rank <= 3