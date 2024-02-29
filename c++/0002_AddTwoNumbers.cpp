// Problem 2: Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 設置一個進位的變數
        int carry = 0;
        
        // 初始化虛擬節點
        ListNode *dummy = nullptr;
        ListNode **curr = &dummy;
        
        // 如果 l1 還沒跑完 或 l2 還沒跑完 或 還有進位
        while (l1 != nullptr || l2 != nullptr || carry > 0){
            // 如果還有值, 將值加入 carry, 指向下一個節點
            if (l1 != nullptr){ 
                carry += l1 -> val;
                l1 = l1 -> next;}

            if (l2 != nullptr){
                carry += l2 -> val;
                l2 = l2 -> next;}
            
            // 將個位數塞入 curr, carry移除個位數
            (*curr) = new ListNode(carry % 10);
            carry /= 10;

            // curr 移至下一個位置
            curr = &((*curr) -> next);
        }
        
        return dummy;
    }
};