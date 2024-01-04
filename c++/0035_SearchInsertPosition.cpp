// Problem 35: Search Insert Position
// https://leetcode.com/problems/search-insert-position/

#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // 先預設答案在 index = 0 的位置
        int output=0;

        // 跑迴圈, 如果目前的值小於目標 就認定目標要在他之後, ans往上加 繼續往後比對
        // 如果 >= 就代表可以加入, 跳脫迴圈
        // 如果跑完 皆小於, ans也是最後的位置
        for (int i=0; i<nums.size(); i++){
            if (nums[i]<target){
                output++;
            }
            else break;
        }
        return output;
    }
};