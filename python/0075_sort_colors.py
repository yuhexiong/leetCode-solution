# Problem 75: Sort Colors
# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        # 先宣告跑的 index 為初始 0, 已經 2 這個數字的開頭 index 為最後(即假設沒有 2)
        i = 0
        head_of_two = len(nums)

        # 跑迴圈直到 i 超過 nums 的長度
        while (i < len(nums)):
            # 如果數字是 0, 將這個數字刪除, 並在最前面加入 0, index + 1 繼續尋找
            if nums[i] == 0:
                del nums[i]
                nums.insert(0, 0)
                i += 1
            # 如果數字是 2, 將這個數字刪除, 並在最後面加入 2, index 不變因為後一個值會往前移到 index
            # 更新 數字 2 的開頭 index 減一
            elif nums[i] == 2:
                del nums[i]
                nums.append(2)
                head_of_two -= 1
            # 如果是 1, index + 1 繼續尋找
            else:
                i += 1

            # 如果 i 的位置等於 數字 2 的開頭 index, 代表後面都是檢查過後的數字 2, 則提早離開迴圈
            if i == head_of_two:
                break
