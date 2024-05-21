# Problem 3147: Taking Maximum Energy From the Mystic Dungeon
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # 先宣告答案是負無窮大
        ans = float('-inf')

        # 宣告和 energy 長度相同的 list, 預設都是 0, 用來記錄每個位置的最大 energy
        dp = [0] * len(energy)

        # 迴圈從最後面開始跑, 先算好後面的, 到前面要使用後面的值時就可以直接加上
        for i in range(len(energy)-1, -1, -1):
            # 這個位置的 dp 為 energy + i+k 位置的 dp, 如果 i+k 已經超出長度則為 0
            dp[i] = energy[i] + (dp[i + k] if i + k < len(energy) else 0)
            # 取得目前 ans 和 dp[i] 較大者
            ans = max(ans, dp[i])
        
        # 回傳 ans
        return ans