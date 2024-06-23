# Problem 1575: Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/

from typing import List


class Solution:
    def count_routes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 紀錄到下個城市時剩餘的油量可以有幾種走法
        dp = [[0] * (fuel + 1) for _ in range(len(locations))]
        # 終點為1
        for remain_fuel in range(fuel + 1):
            dp[finish][remain_fuel] = 1

        for remain_fuel in range(fuel + 1):
            for curr_city in range(len(locations)):
                for next_city in range(len(locations)):
                    # 不處理自己到自己的狀況
                    if curr_city == next_city:
                        continue
                    # 如果剩餘的油量足以支付這段旅程, 將筆數加上去
                    if remain_fuel >= abs(locations[curr_city] - locations[next_city]):
                        dp[curr_city][remain_fuel] += dp[next_city][remain_fuel -
                                                                 abs(locations[curr_city] - locations[next_city])]
                        dp[curr_city][remain_fuel] %= 10**9 + 7

        return dp[start][fuel]
