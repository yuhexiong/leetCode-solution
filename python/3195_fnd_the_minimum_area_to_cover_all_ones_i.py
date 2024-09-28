# Problem 3195: Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

from typing import List

class Solution:
    def minimum_area(self, grid: List[List[int]]) -> int:
        # 宣告四條邊為整個 grid 區域的相反
        # e.g. 最左邊的線設在最右邊, 只要有 1 就一定在他左邊, 即可一路更新到最左邊
        row_first, row_last = len(grid) - 1, 0
        column_first, column_last = len(grid[0]) - 1, 0

        # 跑迴圈看每一個有 1 的位置
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # 更新四邊的值
                    row_first = min(row_first, i)
                    row_last = max(row_last, i)
                    column_first = min(column_first, j)
                    column_last = max(column_last, j)

        # 計算兩邊差額相乘為面積
        return (row_last - row_first + 1) * (column_last - column_first + 1)