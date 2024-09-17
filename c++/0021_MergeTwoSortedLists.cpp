// Problem 21: Merge Two Sorted Lists
// https://leetcode.com/problems/roman-to-integer/

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // 宣告 dummy 第一個 node 為 0, curry 為 dummy 的地址
        ListNode dummy(0);
        ListNode* curry = &dummy;
        
        // 如果 list1 和 list2 都還有值
        while (list1 && list2) {
            // 將比較大的值加入 curry 的下一個 node, 並更新當前 list 指向下一個 node, curry 也指向下一個 node
            if ( list1->val < list2->val ) {
                curry->next = list1;
                list1 = list1->next;
                curry = curry->next;
            }
            else{
                curry->next = list2;
                list2 = list2->next;
                curry = curry->next;
            }
        }
        
        // 如果只剩其中一個 list 有值, 則將 curry 指向剩下的 list
        if (list1) {
            curry->next = list1;
        }
        else if (list2) {
            curry->next = list2;
        }       
        
        // 回傳 dummy 從第二個 node 開始的值
        return dummy.next;
    }
};