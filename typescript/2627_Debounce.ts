// Problem 2627: Debounce
// https://leetcode.com/problems/debounce/

/**
 * Example 1:
 * 
 * Input: 
 * t = 50
 * calls = [
 *   {"t": 50, inputs: [1]},
 *   {"t": 75, inputs: [2]}
 * ]
 * Output: [{"t": 125, inputs: [2]}]
 * 
 * Explanation:
 * let start = Date.now();
 * function log(...inputs) { 
 *   console.log([Date.now() - start, inputs ])
 * }
 * const dlog = debounce(log, 50);
 * setTimeout(() => dlog(1), 50); 代表在 50 ms之後執行 dlog(1)
 * setTimeout(() => dlog(2), 75); 代表在 75 ms之後執行 dlog(2)
 * 這在之前第一個計時器還沒到底 50 ms, 這次調用會清除之前設置的計時器, 重新設置一個新的計時器，以 50 ms 延遲執行
 * 所以第二個調用在 125 ms 時執行
 * 因為前一次調用後的 50 毫秒內沒有新的調用發生, 所以被執行並輸出時間為 125 ms
 */

type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    // 設定一個計時器
    let timer : ReturnType<typeof setTimeout>;

    return function(...args) {
        // 清除之前的計時器
        clearTimeout(timer);
        // 重新設定計時器
        timer = setTimeout(() => fn(...args), t);
    }
};