// Problem 3069: Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        // 先宣告兩個 vector, 並把第一個(index==0)和第二個(index==1)的值放進去
        vector<int>vec1;
        vector<int>vec2;
        vec1.push_back(nums[0]);
        vec2.push_back(nums[1]);

        // 迴圈從index=2開始跑, 依題目所述, 將值加入最後一個值較大的vector
        for (int i = 2; i < nums.size(); i++) {
            if (vec1.back() > vec2.back()) {
                vec1.push_back(nums[i]);
            } else {
                vec2.push_back(nums[i]);
            }
        }

        // 合併兩個 vector
        vec1.insert(vec1.end(), vec2.begin(), vec2.end());
        return vec1;
    }
};