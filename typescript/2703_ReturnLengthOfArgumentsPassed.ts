// Problem 2703: Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

import { JSONValue } from "./types";

function argumentsLength(...args: JSONValue[]): number {
  // 使用 .length 取得長度
	return args.length;
};