# Problem 970: Powerful Integers
# https://leetcode.com/problems/powerful-integers/

from typing import List


class Solution:
    def powerful_integers(self, x: int, y: int, bound: int) -> List[int]:
        # 列出所有小於等於 bound 的 x的次方, y的次方為兩個list
        x_powers = {x**p for p in range(20) if x**p <= bound}
        y_powers = {y**p for p in range(20) if y**p <= bound}
        # 使用雙層迴圈取的兩種數值相加, 且要小於等於 bound
        ans = list(
            {xp + yp for xp in x_powers for yp in y_powers if xp+yp <= bound})
        return ans
