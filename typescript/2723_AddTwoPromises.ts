// Problem 2723: Add Two Promises
// https://leetcode.com/problems/add-two-promises/

type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
  // 使用 Promise.all 讓兩個 Promise 同步處理, 並 await 兩者的結果再相加
  const [num1, num2] = await Promise.all([promise1, promise2]);
  return num1 + num2
};