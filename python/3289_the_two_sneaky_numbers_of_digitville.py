# Problem 3289: The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # 使用 Counter 統計數字出現次數, 並跑迴圈選取次數大於 1 的數字放入 list 回傳
        count = Counter(nums)
        return [num for num, cnt in count.items() if cnt > 1]
