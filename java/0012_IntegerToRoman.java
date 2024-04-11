// Problem 12: Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

import java.util.*;

class Solution {
    public String intToRoman(int num) {
        // 設定整數轉羅馬數字的規則, 由大排到小
        Map<Integer, String> change = new LinkedHashMap<Integer, String>() {{
            put(1000, "M");
            put(900, "CM");
            put(500, "D");
            put(400, "CD");
            put(100, "C");
            put(90, "XC");
            put(50, "L");
            put(40, "XL");
            put(10, "X");
            put(9, "IX");
            put(5, "V");
            put(4, "IV");
            put(1, "I");
        }};

        StringBuilder ans = new StringBuilder();
        // 跑迴圈, 如果現在的 num 大於 change 的數字, ans 就加入羅馬數字, num 減去整數
        for (Map.Entry<Integer, String> entry : change.entrySet()) {
            int integerNum = entry.getKey();
            while (num >= integerNum) {
                ans.append(entry.getValue());
                num -= integerNum;
            }
        }
        return ans.toString();
    }
}
