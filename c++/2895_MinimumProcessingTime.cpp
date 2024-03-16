// Problem 2895: Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        // 將 processorTime 和 tasks 從小排到大
        sort(processorTime.begin(), processorTime.end());
        sort(tasks.begin(), tasks.end());

        // 宣告 pIndex (processorTime 的 index) 要從大跑到小, 宣告 maxTime 預設 0
        int pIndex = processorTime.size() - 1;
        int maxTime = 0;

        // tasks 跑迴圈, 從小跑到大, 依題目比較時間
        for (int i = 0; i < tasks.size(); i++) {
            maxTime = max(maxTime, tasks[i] + processorTime[pIndex]);
            // 每 4 個數字就換到小一個的 processorTime
            if ((i + 1) % 4 == 0) {
                pIndex--;
            }
        }

        return maxTime;
    }
};