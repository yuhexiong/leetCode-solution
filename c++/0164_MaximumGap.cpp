// Problem 164: Maximum Gap
// https://leetcode.com/problems/maximum-gap/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        // 先預設答案是 0
        int ans = 0;

        // 將 nums 從小排到大, 跑迴圈到倒數第二個index, 要計算下一個的值和現在的值的差異
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size()-1; i++) {
            // 如果差異大於 ans, 更新 ans
            if (nums[i+1] - nums[i] > ans) {
                ans = nums[i+1] - nums[i];
            }
        }

        return ans;
    }
};