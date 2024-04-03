// Problem 899: Orderly Queue
// https://leetcode.com/problems/orderly-queue/

import java.util.Arrays;

class Solution {
    public String orderlyQueue(String s, int k) {
        if (k > 1) {
            // 如果 k > 1, 在可以排無限次的情況下, 一定有辦法全部排好
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        } else {
            // 如果 k = 1, 找到所有可能的移動組合，取 lexicographically smallest
            String result = s;
            for (int i = 1; i < s.length(); ++i) {
                String current = s.substring(i) + s.substring(0, i);
                if (current.compareTo(result) < 0) {
                    result = current;
                }
            }
            return result;
        }
    }
}
