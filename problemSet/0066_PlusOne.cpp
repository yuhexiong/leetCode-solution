// Problem 66: Plus One
// https://leetcode.com/problems/plus-one/

#include <vector>

class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        // 在最後一個值 + 1
        digits.back() += 1;
        
        // 從後面跑迴圈回來, 如果等於10就更新為0(因為只+1所以最多10)
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] == 10) {
                digits[i] = 0;
                // 進位, 如果還沒到最前面就把前一個 + 1, 已經到最前面就在前面加一個位數
                if (i != 0) {
                    digits[i - 1] += 1;
                } else {
                    digits.insert(digits.begin(), 1);
                }
            }
        }
        
        return digits;
    }
};
