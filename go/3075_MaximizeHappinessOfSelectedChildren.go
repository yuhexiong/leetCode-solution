// Problem 3075: Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

package Go

import "sort"

//lint:file-ignore U1000 Ignore all unused code
func maximumHappinessSum(happiness []int, k int) int64 {
	// 宣告 ans，並將 happiness 從小排到大
	var ans int64 = 0
	sort.Ints(happiness)

	// 設置 decreasing 紀錄目前的幸福值要減多少，count 紀錄目前取了幾個值
	decreasing := 0
	count := 0

	// 迴圈由後往前跑，幸福值從大取到小
	for i := len(happiness) - 1; i > -1; i-- {
		// 如果現在的幸福值減去 decreasing 已經是負數，就結束迴圈
		if happiness[i]-decreasing < 0 {
			break
		}

		// 將幸福值減去 decreasing 加入 ans，decreasing + 1，count + 1
		ans += int64(happiness[i] - decreasing)
		count += 1
		decreasing += 1

		// 如果以已經取到 k 個就離開迴圈
		if count == k {
			break
		}
	}

	return ans
}
