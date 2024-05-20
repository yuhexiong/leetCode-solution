// Problem 164: Maximum Gap
// https://leetcode.com/problems/maximum-gap/

// 寫由小排到大的 function
int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int maximumGap(int* nums, int numsSize) {
    // 先預設答案是 0
    int ans = 0;

    // 將 nums 從小排到大, 跑迴圈到倒數第二個index, 要計算下一個的值和現在的值的差異
    qsort(nums, numsSize, sizeof(int), cmp);
    for (int i = 0; i < numsSize-1; i++) {
        // 如果差異大於 ans, 更新 ans
        if (nums[i+1] - nums[i] > ans) {
            ans = nums[i+1] - nums[i];
        }
    }

    return ans;
    
}