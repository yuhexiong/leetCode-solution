# Problem 66: Plus One
# https://leetcode.com/problems/plus-one/

from typing import List

class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        # 在最後一個值 + 1
        digits[-1] += 1
        # 從後面跑迴圈回來, 如果等於10就更新為0(因為只+1所以最多10)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                # 進位, 如果還沒到最前面就把前一個 + 1, 已經到最前面就在前面加一個位數
                if i != 0:
                    digits[i-1] += 1
                else: 
                    digits.insert(0, 1)
            
        return digits