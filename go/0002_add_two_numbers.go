// Problem 2: Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

package Go

type ListNode struct {
	Val  int
	Next *ListNode
}

//lint:file-ignore U1000 Ignore all unused code
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// 設置進位的變數
	carry := 0

	// 初始化虛擬節點
	dummy := &ListNode{}
	curr := dummy

	// 如果 l1 還沒跑完 或 l2 還沒跑完 或 還有進位
	for l1 != nil || l2 != nil || carry > 0 {
		// 如果還有值, 將值加入 carry, 指向下一個節點
		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}

		// 將個位數塞入 curr, carry移除個位數
		curr.Next = &ListNode{Val: carry % 10}
		carry /= 10

		// curr 移至下一個位置
		curr = curr.Next
	}

	return dummy.Next
}
