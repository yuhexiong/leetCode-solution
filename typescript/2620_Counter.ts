// Problem 2620: Counter
// https://leetcode.com/problems/counter/

function createCounter(n: number): () => number {
  // 使用 n++, 先回傳n, 再讓它 + 1, 因為第一次不加 1
  return function() {
      return n++;
  }
}