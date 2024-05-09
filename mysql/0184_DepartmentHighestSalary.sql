-- Problem 184: Department Highest Salary
-- https://leetcode.com/problems/department-highest-salary/

-- Write your MySQL query statement below
SELECT 
    Department.name AS 'Department', 
    e1.name AS 'Employee', 
    e1.salary AS 'Salary'
FROM 
    Employee e1
JOIN 
    Department ON e1.departmentId = Department.id
WHERE 
    -- 條件設定為薪水和 薪水最大值 相同的資料
    e1.salary = (SELECT MAX(e2.salary) FROM Employee e2 WHERE e1.departmentId = e2.departmentId);     
