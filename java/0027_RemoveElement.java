// Problem 27: Remove Element
// https://leetcode.com/problems/remove-element/

class Solution {
    public int removeElement(int[] nums, int val) {
        // 預設 count 為 0
        int count = 0;
        
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val) {
                // 跑迴圈計算有幾個不是 val 的數字, 把現在的數值塞到 count 的位置
                nums[count] = nums[i];
                count++;
            }
        }

        return count;
    }
}