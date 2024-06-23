# Problem 6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        # 假如只會有一 row 或 row 的數量比字串長, 就不需要排序
        if num_rows == 1 or num_rows >= len(s):
            return s

        # 宣告 zigzag 模樣的二維陣列, 預設 num_rows 個空字串
        zigzag_ans = [""] * num_rows
        # 宣告起始的 row index 為 0, 從最上面開始
        row_index = 0
        # 宣告一個 boolean 表示現在是不是往下走
        should_move_down = 1

        # 跑迴圈看每個字母
        for letter in s:
            # 如果 should_move_down 為 True 即放置且往下走, False 則往上走再放置
            if should_move_down == 1:
                zigzag_ans[row_index] += letter
                # 如果 row_index 還沒到最後一 row, 就 + 1
                # 如果已經到最後一 row, should_move_down 就設為 False, 改為向上走
                if row_index != num_rows - 1:
                    row_index += 1
                else:
                    should_move_down = 0
            else:
                row_index -= 1
                zigzag_ans[row_index] += letter
                # 如果已經回到第一 row, should_move_down 就設為 True, 並且將 row_index + 1
                if row_index == 0:
                    should_move_down = 1
                    row_index += 1

        # 將所有東西取出成 list, 再用 join 結合成字串
        ans = [y for x in zigzag_ans for y in x]
        return ''.join(map(str, ans))
