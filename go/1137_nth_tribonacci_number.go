// Problem 1137: N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

package Go

//lint:file-ignore U1000 Ignore all unused code
func tribonacci(n int) int {
	// 定義三個變數，分別表示第一個、第二個和第三個 Tribonacci 數
	first, second, third := 0, 1, 1

	if n == 0 {
		// 如果 n == 0，回傳第一個 Tribonacci 數
		return first
	} else if n == 1 {
		// 如果 n == 1，回傳第二個 Tribonacci 數
		return second
	}

	// 從第三個 Tribonacci 數開始計算
	for i := 3; i < n+1; i++ {
		// 計算下一個 Tribonacci 數為 first + second + third, 其他兩個位移
		tmp := first + second + third
		first = second
		second = third
		third = tmp
	}

	// 回傳第 n 個 Tribonacci 數
	return third
}
