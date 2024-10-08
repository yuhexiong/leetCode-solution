// Problem 3263: Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

#include <vector>
using namespace std;

// Definition for doubly-linked list.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node() : val(0), next(nullptr), prev(nullptr) {}
    Node(int x) : val(x), next(nullptr), prev(nullptr) {}
    Node(int x, Node *prev, Node *next) : val(x), next(next), prev(prev) {}
};

class Solution {
public:
	vector<int> toArray(Node *head){
        vector<int> ans;
        while (head) {
            ans.push_back(head -> val);
            head = head -> next;
        }
        return ans;
    }
};