// Problem 3227: Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

package Go

/*
 * 母音的數量為 n 個
 * 如果 n 為 0, Alice 沒有母音可選, Bob 獲勝
 * 如果 n 為大於 0 的偶數, Alice 取 n - 1 個, Bob 只剩 1 可以選, 無法選出偶數個, Alice 獲勝
 * 如果 n 為大於 0 的奇數, Alice 取 n 個, Bob 沒有母音可選, Alice 獲勝
 * 因此只要有找到任一母音, Alice 即獲勝
 */
//lint:file-ignore U1000 Ignore all unused code
func doesAliceWin(s string) bool {
	vowels := map[rune]struct{}{
		'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {},
	}

	for _, letter := range s {
		if _, found := vowels[letter]; found {
			return true
		}
	}

	return false
}
