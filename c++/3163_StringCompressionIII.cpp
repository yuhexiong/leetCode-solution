// Problem 3163: String Compression III
// https://leetcode.com/problems/string-compression-iii/

#include <string>
using namespace std;

class Solution {
public:
    string compressedString(string word) {
        // 宣告 ans 空字串
        string ans = "";

        // 宣告目前的字母是 index 0 的, count 為 1
        char currLetter = word[0];
        int count = 1;
        // 跑迴圈從 index 1 開始算
        for (int i = 1; i < word.size(); i++) {
            // 如果這個字母和前一個字母不同 或 已經到 9 次了, 就結算一次並重新開始計算
            if (word[i] != currLetter || count == 9) {
                ans += to_string(count) + currLetter;
                currLetter = word[i];
                count = 1;
            } else {
                // 其餘就持續 + 1
                count++;
            }
        }

        // 結尾也要結算一次
        ans += to_string(count) + currLetter;
        return ans;
    }
};