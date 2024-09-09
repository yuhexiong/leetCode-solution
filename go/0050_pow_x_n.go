// Problem 50: Pow(x, n)
// https://leetcode.com/problems/powx-n/

package Go

//lint:file-ignore U1000 Ignore all unused code
func myPow(x float64, n int) float64 {
	// 預設答案為 1, 宣告一個取絕對值的 n 為 positiveN
	ans := 1.0
	positive := n >= 0
	positiveN := n
	if !positive {
		positiveN = -n
	}

	// 只要 positiveN 這個次方還沒有到 0, 就持續跑迴圈
	for positiveN > 0 {
		// 如果這個次方是偶數, 就直接把底數平方, 次方除以2, 優化速度
		if positiveN%2 == 0 {
			x *= x
			positiveN /= 2
		}
		// 正常乘一次, 次方減1
		ans *= x
		positiveN--
	}

	// 如果原先 n 是正數就回傳, 負數就回傳導數
	if positive {
		return ans
	}
	return 1 / ans
}
