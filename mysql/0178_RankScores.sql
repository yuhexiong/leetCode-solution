-- Problem 178: Rank Scores
-- https://leetcode.com/problems/rank-scores/

-- Write your MySQL query statement below.
SELECT s2.score,
    -- 統計不同的分數中有幾個高過現在的分數, 設為 rank
    (SELECT COUNT(DISTINCT score) FROM Scores s1 WHERE s1.score >= s2.score) AS `rank`
FROM Scores s2
-- 由大排到小
ORDER BY score DESC;
