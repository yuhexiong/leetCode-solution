// Problem 3024: Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        // 如果兩個短邊加起來小於長邊, 代表無法構成三角形
        if(nums[0] + nums[1] <= nums[2]) return "none";
        // 如果三邊一樣長, 則是正三角形
        if(nums[0] == nums[1] && nums[1] == nums[2]) return "equilateral";
        // 如果某兩邊一樣長(在三邊一樣長已在前面return的情況下), 則是等腰三角形
        if(nums[0] == nums[1] || nums[1] == nums[2]) return "isosceles";
        
        // 其餘都是不等邊三角形
        return "scalene";
    }
};