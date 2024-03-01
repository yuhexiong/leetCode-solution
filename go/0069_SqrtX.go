// Problem 69: Sqrt(x)
// https://leetcode.com/problems/sqrtx/

package Go

//lint:file-ignore U1000 Ignore all unused code
func mySqrt(x int) int {
	r := 0
	// 跑迴圈, 如果目前 r 的平方還小於等於x則 + 1
	for r*r <= x {
		r++
	}
	// 超過 x 才會跳脫, 所以最後要 - 1
	return r - 1
}
