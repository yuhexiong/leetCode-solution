// Problem 35: Search Insert Position
// https://leetcode.com/problems/search-insert-position/

int searchInsert(int* nums, int numsSize, int target) {
    int output = 0;

    // 跑迴圈, 如果目前的值小於目標 就認定目標要在他之後, output 往上加 繼續往後比對
    // 如果 >= 就代表可以加入, 跳脫迴圈
    // 如果跑完 皆小於 output 也是最後的位置
    for (int i = 0; i < numsSize; i++){
        if (nums[i] < target){
            output++;
        }
        else break;
    }
    
    return output;
}