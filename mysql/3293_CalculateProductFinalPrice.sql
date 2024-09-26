-- Problem 3293: Calculate Product Final Price
-- https://leetcode.com/problems/calculate-product-final-price/

-- Write your MySQL query statement below
-- 使用 IFNULL 將沒有折扣的設為 0
SELECT
    Products.product_id, 
    Products.price * (1 - IFNULL(Discounts.discount, 0)/100) AS final_price, 
    Products.category
FROM
    Products 
LEFT JOIN 
    Discounts 
ON Products.category = Discounts.category;