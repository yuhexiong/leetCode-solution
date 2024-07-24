// Problem 154: Find Minimum in Rotated Sorted Array II
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

package Go

//lint:file-ignore U1000 Ignore all unused code
func findMin(nums []int) int {
	// 先宣告最小的數是第 0 個值
	minNum := nums[0]

	// 跑迴圈從第 1 個跑到最後一個
	for i := 1; i < len(nums); i++ {
		// 如果現在的值比最小的數還小, 更新最小的數
		if minNum > nums[i] {
			minNum = nums[i]
		}
		// 如果現在不是最後一個, 且下一個值比現在還小, 即為低谷, 下一個值會是整個陣列中最小的, 直接回傳
		if i != len(nums)-1 && nums[i] > nums[i+1] {
			return nums[i+1]
		}
	}

	// 回傳最小的值
	return minNum
}
