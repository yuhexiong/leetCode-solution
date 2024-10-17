// Problem 2758: Next Day
// https://leetcode.com/problems/next-day/

interface Date {
  nextDay(): string;
}

Date.prototype.nextDay = function(): string {
  // 取得日期後 + 1 再重新設定
  this.setDate(this.getDate() + 1);

  // 將回傳值只取前面 10 個字符
  return this.toISOString().slice(0, 10);
}

/**
* const date = new Date("2014-06-20");
* date.nextDay(); // "2014-06-21"
*/