// Problem 120: Triangle
// https://leetcode.com/problems/triangle/

package Go

import "math"

//lint:file-ignore U1000 Ignore all unused code
func minimumTotal(triangle [][]int) int {
	// 從最下往上, 把左右兩個 child 中小的往上加
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			triangle[i][j] += int(math.Min(float64(triangle[i+1][j]), float64(triangle[i+1][j+1])))
		}
	}
	// 最後頂點就會是最小路徑
	return triangle[0][0]
}
