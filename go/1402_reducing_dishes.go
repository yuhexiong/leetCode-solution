// Problem 1402: Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

package Go

import "sort"

//lint:file-ignore U1000 Ignore all unused code
func maxSatisfaction(satisfaction []int) int {
	// 先將滿意度從低到高排序
	sort.Ints(satisfaction)

	row, ans := 0, 0
	// 從高滿意度開始循環
	for i := len(satisfaction) - 1; i >= 0; i-- {
		// 加上這道菜的分數
		row += satisfaction[i]
		// 如果此次加總造成分數變低則離開迴圈，不計算這次
		if row < 0 {
			break
		}
		// 利用每次 + row 達到元素根據選取幾份菜有加乘幾次
		ans += row
	}

	return ans
}
