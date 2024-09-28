// Problem 3271: Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

#include <string>
using namespace std;

class Solution {
public:
    string stringHash(const string& s, int k) {
        // 宣告答案為空字串
        string ans = "";

        // 跑迴圈, 每次走 k 步, 再在迴圈內把 0 到 k 跑一遍
        for (int i = 0; i < s.length(); i += k) {
            // 宣告每組初始 num 為 0, 跑迴圈看這組數字的相對於 a 的編號是多少並加入
            int num = 0;
            for (int si = 0; si < k; ++si) {
                num += s[i + si] - 'a';
            }

            // 這組算完以後在把數字 mod 26 後換回字母
            ans += static_cast<char>(num % 26 + 'a');
        }

        return ans;
    }
};
