// Problem 154: Find Minimum in Rotated Sorted Array II
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        return *min_element(nums.begin(), nums.end());
    }
};