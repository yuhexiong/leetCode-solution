// Problem 1: Two Sum
// https://leetcode.com/problems/two-sum/

#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // 宣告 result 的空間為兩個整數
    int* result = (int*)malloc(2 * sizeof(int));
    // 設定 returnSize 為 2
    *returnSize = 2;

    // 使用雙層迴圈, 第二層的起點為 i+1 避免重複
    for (int i = 0; i < numsSize; i++){
        for (int j = i + 1; j < numsSize; j++){
            // 相加等於 target 即找到, 回傳 result
            if (nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                return result;
            } 
        }
    }    
    
    return NULL;
}