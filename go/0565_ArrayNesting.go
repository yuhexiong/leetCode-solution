// Problem 565: Array Nesting
// https://leetcode.com/problems/array-nesting/

package Go

//lint:file-ignore U1000 Ignore all unused code
func arrayNesting(nums []int) int {
	// 宣告是否走過這個點的 boolean 陣列, 與預設最大長度為 0
	visit := make([]bool, len(nums))
	longestLen := 0

	// 由每個點都出發過
	for i := 0; i < len(nums); i++ {
		// idx 現在要走的位置, 預設現在的長度為 0
		idx := i
		tepLen := 0

		// 紀錄這點為走過, tepLen + 1, 更新 idx 為指引的下一步位置, 一直走值到該位置已走過
		for !visit[idx] {
			visit[idx] = true
			tepLen++
			idx = nums[idx]
		}

		// 如果 現在的長度 大於 最大長度, 則更新最大長度
		if tepLen > longestLen {
			longestLen = tepLen
		}
	}
	return longestLen
}
