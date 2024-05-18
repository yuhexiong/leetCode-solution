// Problem 3146: Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/description/

package Go

import "math"

//lint:file-ignore U1000 Ignore all unused code
func findPermutationDifference(s string, t string) int {
	// 先跑一個迴圈把 t 內的字母對應 index 存起來
	letterIoIndexInT := make(map[rune]int)
	for i, letter := range t {
		letterIoIndexInT[letter] = i
	}

	// 設一個 diff 變數儲存位置差異
	diff := 0
	// 跑 s 的迴圈, 將剛剛存好的 t 的 index 取出, math.Abs 的參數只支援 float, 出來後再轉 int
	for i, letter := range s {
		indexT := letterIoIndexInT[letter]
		diff += int(math.Abs(float64(i - indexT)))
	}

	return diff
}
