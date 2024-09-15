// Problem 13: Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        // 設定羅馬數字轉整數的規則
        unordered_map <char, int> change = {
            {'I', 1 },
            {'V', 5 }, 
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        // 宣告一個數字
        int num = 0;

        for (int i = 0; i < s.length() - 1; i++){
            // 跑迴圈, 如果現在的羅馬數字筆下一位還要小, 代表是這一位減數, 將數字減去
            if (change[s[i]] < change[s[i+1]]){
                num -= change[s[i]];
            }
            else {
                // 其餘的數都加入
                num += change[s[i]];
            }
        }

        // 將最後一個數加入
        num += change[s.back()];

        // 回傳數字
        return num;
    }
};