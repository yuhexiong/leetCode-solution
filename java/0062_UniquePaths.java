// Problem 62: Unique Paths
// https://leetcode.com/problems/unique-paths/

class Solution {
    public int uniquePaths(int m, int n) {
        // 取得 向右步數 和 向下步數 比較小的
        int minDimension = Math.min(m - 1, n - 1);
        // 計算總步數（向右和向下的總步數）
        int totalMoves = m + n - 2;

        // 預設答案為 1
        long uniquePaths = 1;

        // 使用 C 總步數 取 向右步數 或 C 總步數 取 向下步數
        // C(m+n−2,n−1) = C(m+n−2,m−1)
        // 比較小的會約分掉, 分子只需要跑 minDimension 加乘至 totalMoves, 分母跑 1 至 minDimension
        for (int i = 0; i < minDimension; i++) {
            uniquePaths *= totalMoves - i;
            uniquePaths /= i + 1;
        }

        return (int)uniquePaths;
    }
}