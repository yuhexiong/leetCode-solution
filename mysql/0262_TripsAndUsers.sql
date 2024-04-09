-- Problem 262: Trips and Users
-- https://leetcode.com/problems/trips-and-users/

-- Write your MySQL query statement below
-- 使用 COUNT 和 IF 計算完成數 再 除以總數, 最後用 ROUND 取到小數點第二位
SELECT request_at AS 'Day',
    ROUND((COUNT(IF(status != 'completed', TRUE, NULL)))/(COUNT(*)),2) AS 'Cancellation Rate'
FROM Trips
-- 只選擇 client 和 driver 都沒有 banned 的
JOIN Users d ON Trips.driver_id = d.users_id AND d.banned = 'No'
JOIN Users c ON Trips.client_id = c.users_id AND c.banned = 'No'
-- 限定日期, 再依日期分組
WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY request_at