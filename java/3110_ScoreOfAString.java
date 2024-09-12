// Problem 3110: Score of a String
// https://leetcode.com/problems/score-of-a-string/

class Solution {
    public int scoreOfString(String s) {
        // 預設答案是 0
        int ans = 0;

        // 迴圈從第一個值(跳過第 0 個)跑到最後一個
        for (int i = 1; i < s.length(); i++) {
            // 計算前一個值和現在的值的差, 使用 Math.abs 取絕對值, Java 中不需要額外轉換 ASCII
            ans += Math.abs(s.charAt(i - 1) - s.charAt(i));
        }

        // 回傳答案
        return ans;
    }
}