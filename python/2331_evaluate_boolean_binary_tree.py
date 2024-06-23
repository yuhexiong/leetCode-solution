# Problem 2331: Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 直接依題意寫出每個數字代表的算式, 用遞迴計算下去就可以得出答案
class Solution:
    def evaluate_tree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return self.evaluate_tree(root.right) or self.evaluate_tree(root.left)
        if root.val == 3:
            return self.evaluate_tree(root.right) and self.evaluate_tree(root.left)
