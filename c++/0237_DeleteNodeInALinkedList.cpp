// Problem 237: Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

#include <cstddef>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        // 跳過這個 node
        // 現在的值 指為 下一個的值
        node->val = node->next->val;
        // 下一個的 ListNode 指為 下下一個的 ListNode
        node->next = node->next->next;
    }
};