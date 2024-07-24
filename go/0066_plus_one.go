// Problem 66: Plus One
// https://leetcode.com/problems/plus-one/

package Go

//lint:file-ignore U1000 Ignore all unused code
func plusOne(digits []int) []int {
	// 在最後一個值 + 1
	digits[len(digits)-1] += 1

	// 從後面跑迴圈回來, 如果等於10就更新為0(因為只+1所以最多10)
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] == 10 {
			digits[i] = 0
			// 進位, 如果還沒到最前面就把前一個 + 1, 已經到最前面就在前面加一個位數
			if i != 0 {
				digits[i-1] += 1
			} else {
				digits = append([]int{1}, digits...)
			}
		}
	}

	return digits
}
