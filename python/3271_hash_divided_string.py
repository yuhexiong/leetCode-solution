# Problem 3271: Hash Divided String
# https://leetcode.com/problems/hash-divided-string/

class Solution:
    def string_hash(self, s: str, k: int) -> str:
        # 先宣告答案為空字串
        ans = ""

        # 跑迴圈, 每次走 k 步, 再在迴圈內把 0 到 k 跑一遍
        for i in range(0, len(s), k):
            # 宣告每組初始 num 為 0, 跑迴圈看這組數字的相對於 a 的編號是多少並加入
            num = 0
            for si in range(k):
                num += ord(s[i+si]) - ord('a')

            # 這組算完以後在把數字 mod 26 後換回字母
            ans += chr(num % 26 + ord('a'))

        return ans
