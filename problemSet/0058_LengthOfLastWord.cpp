// Problem 58: Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        // 預設答案是0
        int ans = 0;
        
        // 從後面往前算
        for (int i = s.length()-1; i >= 0; i--){
            if (s[i] == ' ' && ans == 0) { // 如果是結尾的空白格 就不管他
                continue;
            }
            else if (s[i] != ' ') {  // 不是空白格, 開始計數
                ans++;
            }
            else break; // 已經數過了且又遇到空白格, 認定為數完, 離開迴圈
        }
        
        return ans;
    }
};