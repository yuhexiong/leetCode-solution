// Problem 9: Palindrome Number
// https://leetcode.com/problems/palindrome-number/

class Solution {
    public boolean isPalindrome(int x) {
        // 設置是否為回文的boolean, 頭尾數值的int, 和目前位數與最大基數
        boolean palindromeOrNot = false;
        int xFirst, xLast;
        int power = 0;
        int base;

        // 先計算總共幾位數
        int xCount = x;
        while (xCount != 0) {
            power++;
            xCount /= 10;
        }

        while (!palindromeOrNot) {
            if (x < 0)
                break; // 如果已經把x檢查完, 就結束
            if (power < 2) { // 如果x只剩1位數且還在這(while迴圈目前判斷前後都相同), 視為回文並結束
                palindromeOrNot = true;
                break;
            }

            // 更新基數, 取得頭尾
            base = (int) Math.pow(10, power - 1);
            xFirst = x / base;
            xLast = x % 10;

            // 比較頭尾數字
            if (xFirst != xLast)
                break;
            x = x % base - xLast;
            x /= 10;
            power -= 2;
        }
        return palindromeOrNot;
    }
}