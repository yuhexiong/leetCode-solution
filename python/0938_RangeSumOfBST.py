# Problem 938: Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def df(root):
            # 如果到底了, 就回傳 0
            if not root:
                return 0
            # 如果現在的節點的值在範圍內, 回傳他的值 + 左右兩側的所有值
            if root.val >= low and root.val <= high:
                return root.val + df(root.left) + df(root.right)
            # 如果現在的節點的值不在範圍內, 回傳左右兩側的所有值
            return df(root.left) + df(root.right)
        # 從最頂端開始跑
        return df(root)