// Problem 3147: Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        // 先宣告答案是負無窮大
        int ans = INT_MIN;
        // 宣告和 energy 長度相同的 list, 預設都是 0, 用來記錄每個位置的最大 energy
        vector<int> dp(energy.size(), 0);

        // 迴圈從最後面開始跑, 先算好後面的, 到前面要使用後面的值時就可以直接加上
        for (int i = energy.size() - 1; i >= 0; i--) {
            // 這個位置的 dp 為 energy + i+k 位置的 dp, 如果 i+k 已經超出長度則為 0
            dp[i] = energy[i] + (i + k < energy.size() ? dp[i + k] : 0);
            // 取得目前 ans 和 dp[i] 較大者
            ans = max(ans, dp[i]);
        }

        // 回傳 ans
        return ans;
    }
};