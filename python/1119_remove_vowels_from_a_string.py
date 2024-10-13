# Problem 1119: Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def remove_vowels(self, s: str) -> str:
        # 假設答案是空字串, 跑迴圈, 如果當前字母不是 a, e, i, o, u 就加入答案內
        ans = ""

        for c in s:
            if not c in ['a', 'e', 'i', 'o', 'u']:
                ans += c

        return ans
