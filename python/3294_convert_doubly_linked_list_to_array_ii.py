# Problem 3294: Convert Doubly Linked List to Array II
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def to_array(self, node: Optional[Node]) -> List[int]:
        # 先宣告一個空 list
        result = []
        
        # 選取往前的 node
        prev_node = node
        # 跑迴圈, 如果確實有前面的 node 就把值加到最前面, 並往前移一個
        while prev_node:
            result.insert(0, prev_node.val)
            prev_node = prev_node.prev
        
        # 選取往後的 node
        next_node = node.next
        # 跑迴圈, 如果確實有後面的 node 就把值加到最後面, 並往後移一個
        while next_node:
            result.append(next_node.val)
            next_node = next_node.next

        return result