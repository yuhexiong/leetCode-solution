// Problem 2803: Factorial Generator
// https://leetcode.com/problems/factorial-generator/

function* factorial(n: number): Generator<number> {
  if (n == 0) {
    return 1;
  }

  let value: number = 1;
  let count: number = 1;

  while (count <= n) {
    yield value;
    count++;
    value *= count;
  }
}

/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
