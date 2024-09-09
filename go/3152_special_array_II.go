// Problem 3152: Special Array II
// https://leetcode.com/problems/special-array-ii/

package Go

//lint:file-ignore U1000 Ignore all unused code
func isArraySpecialII(nums []int, queries [][]int) []bool {
	// 宣告一個整數 array 放不符合條件的 index
	falseIndex := []int{}
	for i := 0; i < len(nums)-1; i++ {
		if (nums[i]%2 == 0 && nums[i+1]%2 == 0) || (nums[i]%2 == 1 && nums[i+1]%2 == 1) {
			falseIndex = append(falseIndex, i)
		}
	}

	ans := []bool{}
	// 跑迴圈看要求的 subarray 範圍
	for _, query := range queries {
		// 預設沒有找到錯誤
		found := false
		// 跑第二層迴圈看不符合條件的 index, 如果我的 subarray 頭尾內有包含到任一 index, 認為找到錯誤, 紀錄為false
		for _, i := range falseIndex {
			if query[0] <= i && i < query[1] {
				ans = append(ans, false)
				found = true
				break
			}
		}
		// 沒找到, 代表裡面沒有 false, 紀錄為 true
		if !found {
			ans = append(ans, true)
		}
	}

	return ans
}
