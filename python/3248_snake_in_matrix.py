# Problem 3248: Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix/

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # 先跑迴圈把 grid 組出來
        grid = []
        curr_num = 0
        for _ in range(n):
            grid.append([num for num in range(curr_num, curr_num + n)])
            curr_num += n

        # 根據 commands 決定最後停留的 row 和 column 的 index
        r, c = 0, 0
        for command in commands:
            if command == "RIGHT":
                c += 1
            elif command == "LEFT":
                c -= 1
            elif command == "DOWN":
                r += 1
            elif command == "UP":
                r -= 1

        # 將 index 代入找到最後的值
        return grid[r][c]
