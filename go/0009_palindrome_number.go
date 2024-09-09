// Problem 9: Palindrome Number
// https://leetcode.com/problems/palindrome-number/

package Go

import "math"

//lint:file-ignore U1000 Ignore all unused code
func isPalindrome(x int) bool {
	// 設置是否為回文的boolean，頭尾數值的int，以及目前位數和最大基數
	palindromeOrNot := false
	var xFirst, xLast int
	power := 0
	var base int

	// 先計算總共幾位數
	xCount := x
	for xCount != 0 {
		power++
		xCount /= 10
	}

	for !palindromeOrNot {
		if x < 0 {
			break // 如果已經把 x 檢查完，就結束
		}
		if power < 2 { // 如果 x 只剩 1 位數且還在這個 while 迴圈內 (目前判斷前後都相同)，視為回文並結束
			palindromeOrNot = true
			break
		}

		// 更新基數，取得頭尾
		base = int(math.Pow(10, float64(power-1)))
		xFirst = x / base
		xLast = x % 10

		// 比較頭尾數字
		if xFirst != xLast {
			break
		}
		x = x%base - xLast
		x /= 10
		power -= 2
	}
	return palindromeOrNot
}
