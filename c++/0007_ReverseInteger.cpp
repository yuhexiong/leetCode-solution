// Problem 7: Reverse Integer
// https://leetcode.com/problems/reverse-integer/

#include <climits>
class Solution {
public:
    int reverse(int x) {
        // 設置 reverse 的數, 預設為 0, 宣告為 long 才放得下超過 2**31 的數字
        long rev = 0;

        // 迴圈在 x = 0 前都不停止, 每次取出 x 的個位數, 並將 x 換成 x 除以 10 後的整數
        while (x) {
            rev = rev * 10 + x % 10;
            // 如果 rev > 2**31 - 1 或 rev < - 2**31 就設為 0 並離開迴圈
            if (rev > INT_MAX || rev < INT_MIN) {
                rev = 0;
                break;
            }
            x /= 10;
        }

        // 將 rev 轉成 int 再迴傳
        return int(rev);
    }
};