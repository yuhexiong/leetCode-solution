// Problem 2796: Repeat String
// https://leetcode.com/problems/repeat-string/

interface String {
  replicate(times: number): string;
}

String.prototype.replicate = function(times): string {
  // 先宣告空字串再跑迴圈逐次加入
  let repeatString = "";
  for (let i = 0; i < times; i++) {
      repeatString += this;
  }
  return repeatString;
}