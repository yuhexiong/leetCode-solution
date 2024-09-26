-- Problem 1468: Calculate Salaries
-- https://leetcode.com/problems/calculate-salaries/

-- Write your MySQL query statement below
-- 使用 ROUND 四捨五入到整數位
SELECT
    Salaries.company_id, 
    Salaries.employee_id, 
    Salaries.employee_name, 
    ROUND(Salaries.salary * (1 - CompanyTax.tax/100), 0) AS salary  
FROM Salaries 
    -- 另外選取一個表格計算每個 company 的稅率
    LEFT JOIN (
        SELECT 
            company_id,
            CASE 
                WHEN MAX(salary) > 10000 THEN 49
                WHEN MAX(salary) > 1000 THEN 24
                ELSE 0
            END AS tax
        FROM
            Salaries
        GROUP BY company_id
    ) CompanyTax
ON Salaries.company_id = CompanyTax.company_id;