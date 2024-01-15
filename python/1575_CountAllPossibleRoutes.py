# Problem 1575: Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/

from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 紀錄到下個城市時剩餘的油量可以有幾種走法
        dp = [[0] * (fuel + 1) for _ in range(len(locations))]
        # 終點為1
        for remainFuel in range(fuel + 1):
            dp[finish][remainFuel] = 1

        for remainFuel in range(fuel + 1):
            for currCity in range(len(locations)):
                for nextCity in range(len(locations)):
                    # 不處理自己到自己的狀況
                    if currCity == nextCity:
                        continue
                    # 如果剩餘的油量足以支付這段旅程, 將筆數加上去
                    if remainFuel >= abs(locations[currCity] - locations[nextCity]):
                        dp[currCity][remainFuel] += dp[nextCity][remainFuel - abs(locations[currCity] - locations[nextCity])]
                        dp[currCity][remainFuel] %= 10**9 + 7

        return dp[start][fuel]