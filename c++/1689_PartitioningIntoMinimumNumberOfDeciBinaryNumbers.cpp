// Problem 1689 Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPartitions(string n) {
        // 每個位數每次最多 + 1, 所以需要的次數即為最大的數字
        // begin(n), end(n) 相當於跑迴圈, 使用 max_element 取的最大位數
        // - '0' 將字串轉為整數
        return *max_element(begin(n), end(n)) - '0';
    }
};