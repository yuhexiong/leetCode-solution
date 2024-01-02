// Problem 34: Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = -1, end = -1;

        for (int i = 0; i < nums.size(); ++i) {
            // 如果找到 target 且還沒紀錄 start 的位置, 更新 start
            if (nums[i] == target && start == -1) {
                start = i;
            }

            // 如果已經找到 start 且還沒找到 end 且當前數字已經不是 target, 認定前一個是結尾, 更新 end 並跳脫迴圈
            if (start != -1 && end == -1 && nums[i] != target) {
                end = i - 1;
                break;
            }
        }

        // 如果有找到頭 且 沒有結尾, 認定從 start 到底都是 target, 將 end 更新為最後一個位置
        if (start != -1 && end == -1) {
            end = nums.size() - 1;
        }

        return {start, end}; 
    }
};