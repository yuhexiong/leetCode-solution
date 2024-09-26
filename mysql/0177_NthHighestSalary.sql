-- Problem 177: Nth Highest Salary
-- https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    -- 先宣告一個整數 m 為 N - 1
    DECLARE m INT;
    SET m = N - 1;
    RETURN (
        -- Write your MySQL query statement below.
        -- 選擇不重複的薪水值, 由高到低排序, 略過 m 筆, 再只取一筆
        SELECT DISTINCT(salary) FROM Employee ORDER BY salary DESC LIMIT m, 1
    );
END;
