// Problem 58: Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

package Go

import "strings"

//lint:file-ignore U1000 Ignore all unused code
func lengthOfLastWord(s string) int {
	// 去除頭尾的空白
	s = strings.TrimSpace(s)
	// 使用空白字元拆分字串成單字陣列
	words := strings.Fields(s)
	// 回傳最後一個單字的長度
	return len(words[len(words)-1])
}
