// Problem 1422: Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxScore(string s) {
        // 先跑一個迴圈計算所有的1
        int totalOne = 0;
        for (char c : s) {
            if (c == '1') {
                totalOne++;
            }
        }

        int ans = 0;
        int currZero = 0, currOne = 0;

        // 第二個迴圈跑到倒數第一個, 因為切割不能在最後
        for (int i = 0; i < s.size() - 1; ++i) {
            char c = s[i];

            // 統計目前左方所有的 0 和 1 個數
            if (c == '0') {
                currZero++;
            } else {
                currOne++;
            }

            // 在 過去最大結果 和 目前左邊0個數 + 目前右邊1格數 中取最大值
            ans = max(ans, currZero + totalOne - currOne);
        }

        return ans;
    }
};