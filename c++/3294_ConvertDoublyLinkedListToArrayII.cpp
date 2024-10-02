// Problem 3294: Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

#include <string>
#include <vector>
using namespace std;

// Definition for doubly-linked list.
class Node
{
public:
    int val;
    Node *prev;
    Node *next;
    Node() : val(0), next(nullptr), prev(nullptr) {}
    Node(int x) : val(x), next(nullptr), prev(nullptr) {}
    Node(int x, Node *prev, Node *next) : val(x), next(next), prev(prev) {}
};

class Solution
{
public:
    vector<int> toArray(Node *node)
    {
        vector<int> result;

        Node *prev_node = node;
        while (prev_node)
        {
            result.insert(result.begin(), prev_node->val);
            prev_node = prev_node->prev;
        }

        Node *next_node = node->next;
        while (next_node)
        {
            result.push_back(next_node->val);
            next_node = next_node->next;
        }

        return result;
    }
};