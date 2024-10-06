// Problem 3173: Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> orArray(vector<int>& nums) {
        vector<int> ans;
        // 跑迴圈並使用 | 計算後加入資料
        for (int i = 0; i < nums.size() - 1; i++) {
            ans.push_back(nums[i] | nums[i + 1]);
        }
        return ans;
    }
};