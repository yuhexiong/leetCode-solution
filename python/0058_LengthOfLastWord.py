# Problem 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 利用 split 把字串拆成陣列
        wordList = s.split()
        # index -1 取 最後一個值, 再用 len 取得長度
        return len(wordList[-1])