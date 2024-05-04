// Problem 3075: Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

#include <stdio.h>
#include <stdlib.h>

// 寫由小排到大的 function
int cmp(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    // 先宣告 ans, 並將 happiness 從小排到大
    long long ans = 0;
    qsort(happiness, happinessSize, sizeof(int), cmp);

    // 設置 decreasing 紀錄目前的幸福值要減多少, count 紀錄目前取了幾個值
    int decreasing = 0;
    int count = 0;

    // 迴圈由後往前跑, 幸福值從大取到小
    for (int i = happinessSize - 1; i > -1; i--) {
        // 如果現在的幸福值減去 decreasing 已經是負數, 就結束迴圈
        if (happiness[i] - decreasing < 0) {
            break;
        }

        // 將幸福值減去 decreasing 加入 ans, decreasing + 1, count + 1
        ans += happiness[i] - decreasing;
        count += 1;
        decreasing += 1;

        // 如果以已經取到 k 個就離開迴圈
        if (count == k) {
            break;
        }
    }

    return ans;
}