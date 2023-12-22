# Problem 1422: Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        # 先跑一個迴圈計算所有的1
        totalOne = 0
        for c in s:
            if c == '1':
                totalOne += 1

        ans = 0
        currZero, currOne = 0, 0
        # 第二個迴圈跑到倒數第一個, 因為切割不能在最後
        for c in s[:-1]:
            # 統計目前左方所有的 0 和 1 個數
            if c == '0':
                currZero += 1
            else:
                currOne += 1
            # 在 過去最大結果 和 目前左邊0個數 + 目前右邊1格數 中取最大值
            ans = max(ans, currZero + totalOne - currOne)
        return ans