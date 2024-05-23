# Problem 6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 假如只會有一 row 或 row 的數量比字串長, 就不需要排序
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 宣告 zigzag 模樣的二維陣列, 預設 numRows 個空字串
        zigzagAns = [""] * numRows
        # 宣告起始的 row index 為 0, 從最上面開始
        rowIndex = 0
        # 宣告一個 boolean 表示現在是不是往下走
        shouldMoveDown = 1

        # 跑迴圈看每個字母
        for letter in s:
            # 如果 shouldMoveDown 為 True 即放置且往下走, False 則往上走再放置
            if shouldMoveDown == 1:
                zigzagAns[rowIndex] += letter
                # 如果 rowIndex 還沒到最後一 row, 就 + 1
                # 如果已經到最後一 row, shouldMoveDown 就設為 False, 改為向上走
                if rowIndex != numRows - 1:
                    rowIndex += 1
                else:
                    shouldMoveDown = 0
            else:
                rowIndex -= 1
                zigzagAns[rowIndex] += letter
                # 如果已經回到第一 row, shouldMoveDown 就設為 True, 並且將 rowIndex + 1
                if rowIndex == 0:
                    shouldMoveDown = 1
                    rowIndex += 1
                
        # 將所有東西取出成 list, 再用 join 結合成字串
        ans = [ y for x in zigzagAns for y in x]
        return ''.join(map(str,ans))