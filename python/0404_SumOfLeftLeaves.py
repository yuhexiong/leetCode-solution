# Problem 404: Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 增加一個 isLeft 的 boolean 代表是不是左邊的節點, 預設 False
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft: bool = False) -> int:
        # 如果已經到底了, 就回傳 0, 給只有單邊結果的情況使用
        if not root:
            return 0
        # 如果沒有左邊也沒有右邊的話, 自己是左邊就回傳目前的值, 右邊則回傳 0
        if not root.left and not root.right:
            if isLeft:
                return root.val
            else:
                return 0
        # 從 root 開始分左右往下跑
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)