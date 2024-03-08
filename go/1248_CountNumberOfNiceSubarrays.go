// Problem 1248: Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

package Go

//lint:file-ignore U1000 Ignore all unused code
func numberOfSubarrays(nums []int, k int) int {
	// 先把是奇數的位置(index)存下來
	position := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i]%2 == 1 {
			position = append(position, i)
		}
	}

	// 如果奇數個數已經小於 k 則不會有subarray裡面有 k 個基數, 回傳 0
	if len(position) < k {
		return 0
	}

	// 跑迴圈看 position, 從 k-1 開始, 因為前面的奇數個數不足 k
	count := 0
	for posIndex := k - 1; posIndex < len(position); posIndex++ {
		left := 0
		// 如果 posIndex == k-1, 左邊區段個數就是 第一個奇數的位置+1
		if posIndex == k-1 {
			left = position[0] + 1
		} else {
			// position的posIndex-(k-1)位置 為 往回數k-1個奇數位置
			// position的posIndex-k位置 為 往回數k個奇數位置
			// 兩者差距代表左端點在這幾種點上, 所包含的奇數個數不變
			left = position[posIndex-(k-1)] - position[posIndex-k]
		}

		right := 0
		// 如果 posIndex == len(position)-1, 右邊區段個數就是 總長度減去最後一個奇數位置
		if posIndex == len(position)-1 {
			right = len(nums) - position[len(position)-1]
		} else {
			// position的posIndex+1位置 為 往下1個奇數位置
			// position的posIndex位置 為 往這個奇數位置
			// 兩者差距代表右端點在這幾種點上, 所包含的奇數個數不變
			right = position[posIndex+1] - position[posIndex]
		}
		// 左邊的可能數 * 右邊的可能數 = 包含這幾個奇數的總可能數
		count += left * right
	}

	return count
}
