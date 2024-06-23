# Problem 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def add_two_numbers(self, l1, l2):
        # 設置一個進位的變數
        carry = 0

        # 初始化虛擬節點
        dummy = ListNode()
        curr = dummy

        # 如果 l1 還沒跑完 或 l2 還沒跑完 或 還有進位
        while l1 or l2 or carry > 0:
            # 如果還有值, 將值加入 carry, 指向下一個節點
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            # 將個位數塞入 curr, carry移除個位數
            curr.next = ListNode(carry % 10)
            carry //= 10

            # curr 移至下一個位置
            curr = curr.next

        return dummy.next
