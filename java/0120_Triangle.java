// Problem 120: Triangle
// https://leetcode.com/problems/triangle/

import java.util.List;

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        // 從最下往上, 把左右兩個 child 中小的往上加
        for (int i = triangle.size() - 2; i >= 0; i--) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                int minChild = Math.min(triangle.get(i + 1).get(j), triangle.get(i + 1).get(j + 1));
                triangle.get(i).set(j, triangle.get(i).get(j) + minChild);
            }
        }
        // 最後頂點就會是最小路徑
        return triangle.get(0).get(0);
    }
}