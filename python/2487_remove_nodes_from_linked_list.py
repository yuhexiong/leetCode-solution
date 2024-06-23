# Problem 2487: Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 最後一個節點
        if not head:
            return None

        # 計算下一個節點(以遞迴的方式一路搜尋到底)
        head.next = self.remove_nodes(head.next)
        # 如果有下一個節點 且 下一個節點的值比較大, 就跳過目前這個
        if head.next and head.val < head.next.val:
            return head.next

        # 回傳當前的節點
        return head
