# Problem 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def length_of_longest_substring(self, s):

        # 預設答案是 0, 起點是 -1
        ans = 0
        start = -1
        # 宣告一個 dictionary 來放出現過的東西和位置, key: letter, value: index
        appear = {}

        for i, letter in enumerate(s):
            # 如果目前的字母出現過, 且出現的位置在 start 之後, 代表已重複, start 重新計算
            if letter in appear and start <= appear[letter]:
                start = appear[letter]

            # 如果目前還沒有重新計算, 但已經到結尾了, 代表完全沒有重複, ans為整個字串的長度
            if start == -1 and i+1 == len(s):
                ans = len(s)
            # 目前還沒有重複, 更新 ans 為目前長度
            elif start == -1:
                ans = i+1
            # 持續搜尋, 更新 ans 為 過去最大長度 和 目前長度 兩者最大值
            else:
                ans = max(ans, i - start)

            # 更新 letter 出現位置
            appear[letter] = i

        return ans
