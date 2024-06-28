# Problem 3196: Maximize Total Cost of Alternating Subarrays
# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

from typing import List

# Example 1:
# nums = [1, -2, 3, 4]
# dp = [0, nums[0]]

# dp[2] = max(dp[1] + nums[1], dp[0] + nums[0] - nums[1])
# dp[2] = max(nums[0] + nums[1], 0 + nums[0] - nums[1])
# dp[2] = nums[0] - nums[1]

# dp[3] = max(dp[2] + nums[2], dp[1] + nums[1] - nums[2])
# dp[3] = max(nums[0] - nums[1] + nums[2], nums[0] + nums[1] - nums[2])
# dp[3] = nums[0] - nums[1] + nums[2]

# dp[4] = max(dp[3] + nums[3], dp[2] + nums[2] - nums[3])
# dp[4] = max(nums[0] - nums[1] + nums[2] + nums[3], nums[0] - nums[1] + nums[2] - nums[3])
# dp[4] = nums[0] - nums[1] + nums[2] + nums[3]

# 因為翻面的話至少要 2 個 element 才有效果
# 所以我們保留 不包含前 1 個的 sub list 中的最佳解(前 1 個值可以配合目前的翻面) &  包含前 1 個的 sub list 中的最佳解
# 從兩者中選出搭配現在的值的最大數值
# 持續計算到最後是最優解答

class Solution:
    def maximum_total_cost(self, nums: List[int]) -> int:
        dp = [0, nums[0]]
        for i in range(len(nums)-1):
            dp.append(max(dp[-1] + nums[i+1], dp[-2] + nums[i] - nums[i+1]))
        return dp[-1]