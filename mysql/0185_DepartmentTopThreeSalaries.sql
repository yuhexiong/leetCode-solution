-- Problem 185: Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/

-- Write your MySQL query statement below
SELECT Department.name AS 'Department', e1.name AS 'Employee', e1.salary AS 'Salary'
FROM Employee e1
JOIN Department ON e1.departmentId = Department.id
-- HAVING 濾除自定義的資料
-- 使用子查詢找出同 Department 的所有 Employee (叫 e2), 高過 e1 的人數要小於 3
HAVING (SELECT COUNT(DISTINCT e2.salary)
        FROM Employee e2
        WHERE e2.salary > e1.salary
        AND e1.departmentId = e2.departmentId) < 3