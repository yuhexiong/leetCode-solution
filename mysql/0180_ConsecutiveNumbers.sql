-- Problem 180: Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/

-- Write your MySQL query statement below.
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs
-- 條件為下一組 (id + 1, num) 和 下下一組 (id + 2, num) 有出現在表格內
WHERE (id + 1, num) IN (SELECT * FROM Logs) AND (id + 2, num) IN (SELECT * FROM Logs)