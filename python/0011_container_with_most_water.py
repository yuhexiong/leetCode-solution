# Problem 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 宣告 area 與左右兩邊的 index
        area = 0
        left = 0
        right = len(height)-1

        # 跑迴圈直到左邊和右邊的 index 相等
        while left != right:
            # 如果右邊的高度比左邊高, 則 tmp_area 以右邊的高度 * 寬度
            if height[right] > height[left]:
                tmp_area = height[left]*(right-left)
                # 計算完以後淘汰左邊, 如果左邊新高度沒有比舊高度高, 則再持續淘汰
                left += 1
                while height[left-1] > height[left]:
                    left += 1
            # 如果左邊的高度比右邊高, 則 tmp_area 以左邊的高度 * 寬度
            else:
                tmp_area = height[right]*(right-left)
                # 計算完以後淘汰右邊, 如果右邊新高度沒有比舊高度高, 則再持續淘汰
                right -= 1
                while height[right+1] > height[right]:
                    right -= 1

            # 更新 area 為現在和 tmp_area 之中較大者
            area = max(area, tmp_area)

        # 回傳 area
        return area
