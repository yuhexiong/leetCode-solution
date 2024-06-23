# Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        # 使用 enumerate 取得當前 index 和 數值
        for i, num in enumerate(nums):
            # 如果 希望的值(目標減去當前數值) 在這個list中 且 不是同一個位置的值(index不相同)
            # 就視為找到答案, 直接return
            if target - num in nums and i != nums.index(target - num):
                return i, nums.index(target - num)
