# Problem 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def length_of_last_word(self, s: str) -> int:
        # 利用 split 把字串拆成陣列
        word_list = s.split()
        # index -1 取 最後一個值, 再用 len 取得長度
        return len(word_list[-1])
