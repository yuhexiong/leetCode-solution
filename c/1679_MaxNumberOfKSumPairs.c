// Problem 1679: Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

// 寫由小排到大的 function
int cmp(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int maxOperations(int* nums, int numsSize, int k){
    // 設定i, j 為開頭和結尾的 index, operation 為操作次數, 預設 0
    int i = 0; 
    int j = numsSize - 1;
    int operation = 0;

    // 將 nums 從小排到大
    qsort(nums, numsSize, sizeof(int), cmp);

    // 只要 i 小於 j, 即瀏覽的數字還沒有交錯, 則繼續
    while (i < j) {
        int currSum = nums[i] + nums[j];

        // 如果符合我們的相加結果, operation + 1, i 往右邊一格繼續, j 往左邊一格繼續
        if (currSum == k) {
            operation += 1;
            i += 1;
            j -= 1;
        } else if (currSum > k) { // 大於則代表 j 的位置的數字太大, j 往左邊一格繼續
            j -= 1;
        } else { // 小於則代表 i 的位置的數字太小, i 往右邊一格繼續
            i += 1;
        }
    }

    return operation;
}