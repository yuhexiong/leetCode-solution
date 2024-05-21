// Problem 3151: Special Array I
// https://leetcode.com/problems/permutation-difference-between-two-strings/

package Go

//lint:file-ignore U1000 Ignore all unused code
func isArraySpecial(nums []int) bool {
	// 跑迴圈到倒數第二個 index
	for i := 0; i < len(nums)-1; i++ {
		// 如果 現在的質和下一個值都是偶數 或 現在的質和下一個值都是奇數, 回傳 false
		if (nums[i]%2 == 0 && nums[i+1]%2 == 0) || (nums[i]%2 == 1 && nums[i+1]%2 == 1) {
			return false
		}
	}

	// 迴圈跑完都還沒回傳代表沒有錯誤, 回傳 true
	return true
}
