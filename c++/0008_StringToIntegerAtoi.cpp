// Problem 8: String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

#include <climits>
#include <string>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        // 如果 s 是空字串, 就直接回傳 0
        if (s == "") {
            return 0;
        }

        // 宣告 ans 為 0, 起始 index 為 0, 以及符號為正
        long ans = 0;
        int startIndex = 0;
        int symbol = 1;

        // 如果前面有空格可以移除
        while(s[startIndex] == ' ') {
            startIndex += 1;
            // 如果到最後都是空格就可以直接回傳
            if (startIndex == s.size()) {
                return 0;
            }
        }
        
        // 如果 startIndex 的位置是符號就判斷 symbol, 並將 startIndex 移到下一個位置
        if (s[startIndex] == '-') {
            symbol = -1;
            startIndex += 1;
        } else if (s[startIndex] == '+') {
            startIndex += 1;
        }

        // 從 startIndex 開始跑迴圈到結束
        for (int i = startIndex; i < s.size(); i++) {
            // 是數字就加入, 不是數字就離開迴圈
            if (s[i] >= '0' && s[i] <= '9') {
                ans = ans*10 + (s[i] - '0');
            } else {
                break;
            }

            // 每次檢查是否有大於 2 ** 31 - 1 或 小於 - 2 ** 31, 避免超出太多導致 long 溢位
            if (ans * symbol > INT_MAX) {
                return int(INT_MAX);
            } else if (ans * symbol < INT_MIN) {
                return int(INT_MIN);
            }
        }

        // 回傳 ans 加上符號後轉為 int
        return int(ans * symbol);
    }
};