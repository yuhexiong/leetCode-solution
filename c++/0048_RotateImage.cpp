// Problem 48 Rotate Image
// https://leetcode.com/problems/rotate-image/

#include <vector>
using namespace std;

/**
 * Example 2:
 * matrix = [
 *  [ 5, 1, 9,11],
 *  [ 2, 4, 8,10],
 *  [13, 3, 6, 7],
 *  [15,14,12,16]]
 * 
 * 以 example 2 為例, 
 * 第一個 i 決定最外圈, j 決定第一個值: 5 -> 11 -> 16 -> 15 
 * 第一個 i 決定最外圈, j 決定第二個值: 1 -> 10 -> 12 -> 13 
 * 第一個 i 決定最外圈, j 決定第三個值: 9 ->  7 -> 14 ->  2 
 * 第二個 i 決定第二外圈, j 決定第一個值: 4 ->  8 -> 6 ->  3 
 * 
*/

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // 取得矩陣有多少 row, jn 為 index, 設定為 row - 1, 代表最後一列 column
        int n = matrix.size(); 
        int jn = n - 1;  

        // 迴圈跑矩陣一半的 row, 左半部(< jn)的 column
        // 藉由內部的操作, 相當於第一層迴圈決定跑多外層, 第二層迴圈決定跑自第幾個值
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < jn; j++) {
                // 將四個邊角進行值的交換
                int temp = matrix[i][i+j];
                matrix[i][i+j] = matrix[n-1-j-i][i];
                matrix[n-1-j-i][i] = matrix[n-1-i][n-1-i-j];
                matrix[n-1-i][n-1-i-j] = matrix[i+j][n-1-i];
                matrix[i+j][n-1-i] = temp;
            }
            // 因為以一層外圈為基礎, 所以是 jn - 2
            jn -= 2;
        }
    }
};