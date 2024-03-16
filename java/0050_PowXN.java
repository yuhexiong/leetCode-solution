class Solution {
    public double myPow(double x, int n) {
        // 預設答案為 1, 宣告一個取絕對值的 n 為 positiveN
        double ans = 1;
        boolean positive = n >= 0;
        long positiveN = (positive) ? n : -(long) n;

        // 只要 positiveN 這個次方還沒有到 0, 就持續跑迴圈
        while (positiveN > 0) {
            // 如果這個次方是偶數, 就直接把底數平方, 次方除以2, 優化速度
            if (positiveN % 2 == 0) {
                x *= x;
                positiveN /= 2;
            }
            // 正常乘一次, 次方減1
            ans *= x;
            positiveN--;
        }
        
        // 如果原先 n 是正數就回傳, 負數就回傳導數
        return (positive) ? ans : 1 / ans;
    }
}
