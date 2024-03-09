// Problem 3005: Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        // 先跑一個迴圈統計數字出現次數
        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num]++;
        }

        // 取得每組配對中值(次數)最大的, 用 second 取得值(次數)
        int maxFreq = 0;
        for (const auto& pair : freq) {
            maxFreq = max(maxFreq, pair.second);
        }

        // 如果有值(次數) == maxFreq, 就這個數加入 count
        int count = 0;
        for (const auto& pair : freq) {
            if (pair.second == maxFreq) {
                count += pair.second;
            }
        }

        return count;
    }
};