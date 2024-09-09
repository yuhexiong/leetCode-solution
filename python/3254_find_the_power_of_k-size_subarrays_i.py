# Problem 3254: Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

from typing import List


class Solution:
    def results_array(self, nums: List[int], k: int) -> List[int]:
        # 開一個空 list 放答案
        ans = []

        # 迴圈跑 len(nums)-k+1 次, 因為要長度 k 才能組成一個 sublist
        for i in range(len(nums)-k+1):
            # 先建立 increasing 的 list
            increasing_list = [increasing_num + nums[i]
                               for increasing_num in range(k)]

            # 如果這段 sublist 和 increasing 的 list 相同, 就添加裡面最大的, 不同就添加 -1
            if nums[i:i+k] == increasing_list:
                ans.append(max(nums[i:i+k]))
            else:
                ans.append(-1)

        # 回傳 ans
        return ans
