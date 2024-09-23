-- Problem 1821: Find Customers With Positive Revenue this Year
-- https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

-- Write your MySQL query statement below
-- 選擇 DISTINCT 才不會有重複的 id
SELECT 
DISTINCT customer_id 
FROM Customers
WHERE year = '2021' AND revenue > 0;