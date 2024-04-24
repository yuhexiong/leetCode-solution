// Problem 1137: N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

#include <vector>
using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        // 定義三個變數，分別表示第一個、第二個和第三個 Tribonacci 數
        int first = 0, second = 1, third = 1;

        // 如果 n == 0，回傳第一個 Tribonacci 數
        if (n == 0) {
            return first;
        } 
        // 如果 n == 1，回傳第二個 Tribonacci 數
        else if (n == 1) {
            return second;
        }

        // 從第三個 Tribonacci 數開始計算
        for (int i = 3; i < n + 1; i++) {
            // 計算下一個 Tribonacci 數為 first + second + third, 其他兩個位移
            int tmp = first + second + third;
            first = second;
            second = third;
            third = tmp;
        }

        // 回傳第 n 個 Tribonacci 數
        return third;
    }
};
