// Problem 1: Two Sum
// https://leetcode.com/problems/two-sum/

#include <vector>
using namespace std;

class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        // 宣告回傳的型態
        vector<int> result;
        // 使用雙層迴圈, 第二層的起點為 i+1 避免重複
        for (int i = 0; i < nums.size(); i++){
            for (int j = i + 1; j < nums.size(); j++){
                // 相加等於 target 即找到, 離開迴圈
                if (nums[i] + nums[j] == target){
                    result.push_back(i);
                    result.push_back(j);
                    break;
                } 
            }
        }    
    return result;
    }
};