# Problem 3259: Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

from typing import List


class Solution:
    def max_energy_boost(self, energy_drink_a: List[int], energy_drink_b: List[int]) -> int:
        # 從倒數第二個開始往前跑
        # 如果是倒數第二個, 選擇就只有自己這個 list 的最後一個
        # 如果是倒數第二個以前, 選擇就有自己這個 list 的下一個 或 另外一個 list 的下下一個
        # 利用由後往前算來把之後所有可能的最大值加在自己這個值上, 最後 index = 0 的位置的值就是最好的選擇
        for i in range(len(energy_drink_a)-2, -1, -1):
            if i >= len(energy_drink_a)-2:
                energy_drink_a[i] += energy_drink_a[i+1]
                energy_drink_b[i] += energy_drink_b[i+1]
            else:
                energy_drink_a[i] += max(energy_drink_a[i+1],
                                         energy_drink_b[i+2])
                energy_drink_b[i] += max(energy_drink_b[i+1],
                                         energy_drink_a[i+2])

        return max(energy_drink_a[0], energy_drink_b[0])
