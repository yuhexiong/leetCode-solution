// Problem 1402: Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

import java.util.Arrays;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        // 先把菜從低分排到高分
        Arrays.sort(satisfaction);

        int row = 0, ans = 0;
        // 從高分跑迴圈回來
        for (int i = satisfaction.length - 1; i >= 0; --i) {
            // 加上這道菜的分數
            row += satisfaction[i];
            // 如果此次加總造成分數變低則離開迴圈, 不計算這次
            if (row < 0) {
                break;
            }
            // 利用每次 + row 達到 element 根據選取幾份菜有加乘幾次
            ans += row;
        }

        return ans;
    }
}
