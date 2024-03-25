// Problem 12: Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        // 設定整數轉羅馬數字的規則, 由大排到小
        vector<pair<int, string>> change =  {
            {1000, "M"}, {900, "CM"}, 
            {500, "D"}, {400, "CD"}, 
            {100, "C"}, {90, "XC"}, 
            {50, "L"}, {40, "XL"}, 
            {10, "X"}, {9, "IX"}, 
            {5, "V"}, {4, "IV"}, 
            {1, "I"}};
        
        string ans = "";
        // 跑迴圈, 如果現在的 num 大於 change 的數字, ans 就加入羅馬數字, num 減去整數
        for (auto& pair : change) {
            int integerNum = pair.first;
            while (num >= integerNum) {
                ans += pair.second;
                num -= integerNum;
            }
        }
        return ans;
    }
};