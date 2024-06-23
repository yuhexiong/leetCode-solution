# Problem 1289: Minimum Falling Path Sum II
# https://leetcode.com/problems/minimum-falling-path-sum-ii/

from typing import List


class Solution:
    def min_falling_path_sum(self, grid: List[List[int]]) -> int:
        # 跳過第 0 row, 從上往下更新, 每個值會從前一 row 中除了自己正上方的以外的值中挑出最小的加進去
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += min(grid[i-1][:j]+grid[i-1][j+1:])
        # 到最後一 row, 取最小的值
        return min(grid[-1])
