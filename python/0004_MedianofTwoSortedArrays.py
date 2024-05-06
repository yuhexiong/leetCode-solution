# Problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 串接兩個 list 並排序
        nums = nums1 + nums2
        nums.sort()

        # 如果這個list有奇數個, 取中間值; 偶數個, 取中央兩個相加的平均
        # // 為 地板除法, 除完後取整數
        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2] 
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2