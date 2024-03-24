// Problem 2828: Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        // 如果 words 的長度 和 s 的長度不相同, 回傳 false
        if (words.size() != s.size()) {
            return false;
        }

        // 跑迴圈比較每一個單字的第一個字母和s的第一個字母, 不相同則回傳 false
        for (int i = 0; i < words.size(); i++) {
            if (words[i][0] != s[i]) {
                return false;
            }
        }
        
        // 跑完迴圈還沒回傳, 代表字母都相同, 回傳 true
        return true;
    }
};