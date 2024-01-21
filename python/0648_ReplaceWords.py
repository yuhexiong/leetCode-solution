# Problem 648: Replace Words
# https://leetcode.com/problems/replace-words/

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 宣告放取代好的字的 list
        ans = []
        # 將句子拆成單字跑迴圈
        for word in sentence.split():
            # 從單字開頭開始跑迴圈, 找到有在 dictionary 的就加入解答並脫離迴圈
            for i in range(len(word)):
                if word[:i] in dictionary:
                    ans.append(word[:i])
                    break
            # 如果整個 dictionary 都檢查過, 確認沒有(沒有 break), 就把原本的單字加進去
            else:
                ans.append(word)
        return ' '.join(ans)