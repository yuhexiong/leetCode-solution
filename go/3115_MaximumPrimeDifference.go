// Problem 3115: Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

package Go

//lint:file-ignore U1000 Ignore all unused code
func isPrime(num int) bool {
	if num == 1 {
		return false
	}

	divisor := 2
	for divisor*divisor <= num {
		if num%divisor == 0 {
			return false
		}
		divisor += 1
	}
	return true
}

func maximumPrimeDifference(nums []int) int {
	// 跑迴圈找左邊的質數
	leftIndex := 0
	for i := 0; i < len(nums); i++ {
		if isPrime(nums[i]) {
			leftIndex = i
			break
		}
	}

	// 跑迴圈從後面往回找右邊的質數, 最多找到 leftIndex 後面一個, 沒找到就使用 leftIndex
	rightIndex := leftIndex
	for i := len(nums) - 1; i > leftIndex; i-- {
		if isPrime(nums[i]) {
			rightIndex = i
			break
		}
	}

	return rightIndex - leftIndex
}
