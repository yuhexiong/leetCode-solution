# Problem 771: Jewels and Stones
# https://leetcode.com/problems/plus-one/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 設一個 set 收集 jewels 的字母
        jewelSet = set(jewels)
        # 跑迴圈加總 stone 是否在 set 中
        return sum(stone in jewelSet for stone in stones)