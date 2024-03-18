// Problem 66: Plus One
// https://leetcode.com/problems/plus-one/

import java.util.*;

class Solution {
    public int[] plusOne(int[] digits) {
        // 在最後一個值 + 1
        digits[digits.length - 1] += 1;
        
        // 從後面跑迴圈回來, 如果等於10就更新為0(因為只+1所以最多10)
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] == 10) {
                digits[i] = 0;
                // 進位, 如果還沒到最前面就把前一個 + 1, 已經到最前面就在前面加一個位數
                if (i != 0) {
                    digits[i - 1] += 1;
                } else {
                    // 如果已經到最前面就在前面加一個位數
                    int[] result = new int[digits.length + 1];
                    result[0] = 1;
                    for (int j = 1; j < result.length; j++) {
                        result[j] = digits[j - 1];
                    }
                    return result;
                }
            }
        }
        
        return digits;
    }
};
