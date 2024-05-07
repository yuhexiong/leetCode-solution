// Problem 2715: Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

import { JSONValue } from "./types";

type Fn = (...args: JSONValue[]) => void

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
  // 定義清除 timeout 的 function
  const cancelFn: Function = () => {
    clearTimeout(timer);
  };

  // 設置計時器, 在t秒後執行fn
  const timer = setTimeout(() => {
    fn(...args);
  }, t);

  // 回傳 取消的 function
  return cancelFn;
};
