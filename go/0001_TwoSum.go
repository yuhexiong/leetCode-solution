// Problem 1: Two Sum
// https://leetcode.com/problems/two-sum/

package Go

//lint:file-ignore U1000 Ignore all unused code
func twoSum(nums []int, target int) []int {
	n := len(nums)
	// 宣告回傳的型態
	var output []int

	// 使用雙層迴圈, 第二層的起點為 i+1 避免重複
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			// 相加等於 target 即找到, 離開迴圈
			if nums[i]+nums[j] == target {
				output = []int{i, j}
				break
			}
		}
	}
	return output
}
