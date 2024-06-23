# Problem 17: Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from functools import reduce
from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        # 先預設每個數字對應的英文字母
        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # 如果沒有數字就直接 return 空陣列
        if digits == "":
            return []
        # 把數字對應到英文並整理成list
        letter = [maps[i] for i in digits]
        # 使用雙層迴圈跑所有排列組合
        return reduce((lambda x, y: [i + j for i in x for j in y]), letter)
