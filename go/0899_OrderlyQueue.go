// Problem 899: Orderly Queue
// https://leetcode.com/problems/orderly-queue/

package Go

import (
	"sort"
	"strings"
)

//lint:file-ignore U1000 Ignore all unused code
func orderlyQueue(s string, k int) string {
	if k > 1 {
		// 如果 k > 1, 在可以排無限次的情況下, 一定有辦法全部排好
		str := strings.Split(s, "")
		sort.Strings(str)
		return strings.Join(str, "")
	} else {
		// 如果 k = 1, 找到所有可能的移動組合，取 lexicographically smallest
		result := s
		for i := 1; i < len(s); i++ {
			newStr := s[i:] + s[:i]
			if newStr < result {
				result = newStr
			}
		}

		return result
	}
}
