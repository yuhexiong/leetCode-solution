-- Problem 3204: Bitwise User Permissions Analysis
-- https://leetcode.com/problems/bitwise-user-permissions-analysis/

-- Write your MySQL query statement below
-- 使用 BIT_AND 和 BIT_OR 來對所有 permissions 進行位元運算
SELECT 
    BIT_AND(permissions) AS common_perms,
    BIT_OR(permissions) AS any_perms
FROM user_permissions;