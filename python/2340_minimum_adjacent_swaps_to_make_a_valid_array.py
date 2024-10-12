# Problem 2340: Minimum Adjacent Swaps to Make a Valid Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

from typing import List


class Solution:
    def minimum_swaps(self, nums: List[int]) -> int:
        # 假設最小值的位置和值為第 0 個, 跑迴圈更新為正確值
        min_index = 0
        min_num = nums[min_index]
        for i in range(1, len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                min_index = i

        # 找到最小值後更新 nums, 將最小值移到最左邊
        nums = [nums[min_index]] + nums[:min_index] + nums[min_index + 1:]

        # 假設最大值的位置和值為最後一個, 跑迴圈更新為正確值
        max_index = len(nums) - 1
        max_num = nums[max_index]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i

        # 移動的步數為最小值的 index 和 0 的距離 + 最大值的 index 和 len(nums) - 1 的距離
        return min_index + len(nums) - 1 - max_index
