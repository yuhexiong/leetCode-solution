-- Problem 2989: Class Performance
-- https://leetcode.com/problems/class-performance/

-- Write your MySQL query statement below
-- 直接使用 MAX 和 MIN 來選取最大值與最小值相減
SELECT (
    MAX(assignment1 + assignment2 + assignment3) - MIN(assignment1 + assignment2 + assignment3)
) AS difference_in_score
FROM Scores;