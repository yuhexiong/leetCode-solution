# Problem 771: Jewels and Stones
# https://leetcode.com/problems/plus-one/

class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        # 設一個 set 收集 jewels 的字母
        jewel_set = set(jewels)
        # 跑迴圈加總 stone 是否在 set 中
        return sum(stone in jewel_set for stone in stones)
