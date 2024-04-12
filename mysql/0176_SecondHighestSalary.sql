-- Problem 176: Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/

-- Write your MySQL query statement below
SELECT (
-- 選擇不重複的薪水值, 由高到低排序, 略過一筆, 再只取一筆
    SELECT DISTINCT salary 
    FROM Employee 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary
-- 再重新命名欄位