// Problem 1248: Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

import java.util.ArrayList;

class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        // 先把是奇數的位置(index)存下來
        ArrayList<Integer> position = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 1) {
                position.add(i);
            }
        }

        // 如果奇數個數已經小於 k 則不會有subarray裡面有 k 個基數, 回傳 0
        if (position.size() < k) {
            return 0;
        }

        // 跑迴圈看 position, 從 k-1 開始, 因為前面的奇數個數不足 k
        int count = 0;
        for (int posIndex = k - 1; posIndex < position.size(); posIndex++) {
            int left = 0;
            // 如果 posIndex == k-1, 左邊區段個數就是 第一個奇數的位置+1
            if (posIndex == k - 1) {
                left = position.get(0) + 1;
            } else {
                // position 的 posIndex-(k-1) 位置 為 往回數 k-1 個奇數位置
                // position 的 posIndex-k 位置 為 往回數 k 個奇數位置
                // 兩者差距代表左端點在這幾種點上, 所包含的奇數個數不變
                left = position.get(posIndex - (k - 1)) - position.get(posIndex - k);
            }

            int right = 0;
            // 如果 posIndex == position.size()-1, 右邊區段個數就是 總長度減去最後一個奇數位置
            if (posIndex == position.size() - 1) {
                right = nums.length - position.get(position.size() - 1);
            } else {
                // position 的 posIndex+1 位置 為 往下 1 個奇數位置
                // position 的 posIndex 位置 為 往這個奇數位置
                // 兩者差距代表右端點在這幾種點上, 所包含的奇數個數不變
                right = position.get(posIndex + 1) - position.get(posIndex);
            }
            // 左邊的可能數 * 右邊的可能數 = 包含這幾個奇數的總可能數
            count += left * right;
        }

        return count;
    }
}
