# Problem 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 設定 start, end 位置答案皆為 -1
        start = end = -1

        for i in range(len(nums)):
            # 如果找到 target 且還沒紀錄 start 的位置, 更新 start
            if nums[i] == target and start == -1:
                start = i
            # 如果已經找到 start 且 還沒找到end 且當前數字已經不是 target, 認定前一個是結尾, 更新 end 並跳脫迴圈
            if start > -1 and end == -1 and nums[i] != target:
                end = i-1
                break
        # 如果有找到頭 且 沒有結尾, 認定從 start 到底都是 target, 將 end 更新為最後一個位置
        if start >- 1 and end == -1:
            end = len(nums) - 1
        return [start, end]