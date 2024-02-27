// Problem 120: Triangle
// https://leetcode.com/problems/triangle/

#include <string>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // 從最下往上, 把左右兩個 child 中小的往上加
        for (int i = triangle.size() - 2; i >= 0; --i) {
            for (int j = 0; j < triangle[i].size(); ++j) {
                triangle[i][j] += std::min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        // 最後頂點就會是最小路徑
        return triangle[0][0];
    }
};