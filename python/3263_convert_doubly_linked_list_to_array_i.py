# Problem 3263: Convert Doubly Linked List to Array I
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def to_array(self, root: Optional[Node]) -> List[int]:
        # 開空的 list 跑迴圈把 node 的值一個一個加在後面
        ans = []
        while root:
            ans.append(root.val)
            root = root.next
        return ans
        