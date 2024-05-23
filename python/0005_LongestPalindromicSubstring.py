# Problem 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 先宣告長度和中心是 0
        longest = 0
        center = 0

        # 假如這個 Palindrome 是奇數, center不用對稱
        for i in range(len(s) - 2):
            # 假如這個值和下下一個值相同(下一個值預定為 center), 則以這兩個為基準往左與往右比較差異
            if s[i] == s[i+2]:
                # 預設 count 是 3 (center 與左右兩個值)
                count = 3
                # step 為總共要比較的步數, 取 i 往左算到最前面 和 i+2 往右算到最後面 兩者間較小的
                step = min(i, len(s)-1-(i+2))
                # 迴圈跑 2 到 step+2, 因為位置是由中心加減2開始, 總步數還是 step, 每一組值相同 count 就加 2
                for j in range(2, step + 2):
                    if s[i+1-j] == s[i+1+j]:
                        count += 2
                    else:
                        break
                # 如果這組是目前最長, 更新 longest, center 如前面所述是 i+1
                if count > longest:
                    longest = count
                    center = i+1
        
        # 假如這個 Palindrome 是偶數
        for i in range(len(s) - 1):
            # 假如這個值和下一個值相同, 則以這兩個為基準往左與往右比較差異
            if s[i] == s[i+1]:
                # 預設 count 是 2 (左右兩個值, center 設為左邊的值)
                count = 2
                # step 為總共要比較的步數, 取 i 往左算到最前面 和 i+1 往右算到最後面 兩者間較小的
                step = min(i, len(s)-1-(i+1))
                # 迴圈跑 1 到 step+1, 因為位置是由 i 和 i+1 開始, 總步數還是 step, 每一組值相同 count 就加 2
                for j in range(1, step+1):
                    if s[i-j] == s[i+1+j]:
                        count += 2
                    else:
                        break
                # 如果這組是目前最長, 更新 longest, center 如前面所述是 i
                if count > longest:
                    longest = count
                    center = i

        # 假如 longest 是 0, 依題目所述 list 中至少有一個值, 回傳第一個(index = 0)值
        if longest == 0:
            return s[0]
        # 依照 longest 是奇數還是偶數, 搭配上面設置的 center 位置取的子陣列
        elif longest%2 == 1:
            return s[center - (longest-1)//2 : center + (longest+1)//2]
        else:
            return s[center - longest//2 + 1 : center + 1 + longest//2]