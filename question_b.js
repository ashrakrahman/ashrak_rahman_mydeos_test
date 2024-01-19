/**
 * Author: Ashrak Rahman Lipu
 *
 * Question B: The goal of this question is to write a software library that accepts 2 version string as
            input and returns whether one is greater than, equal, or less than the other.
            As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
 *
 */

const validator = (vNmae) => {
  if (!vNmae) return false;
  return true;
};

const compareFunction = (v1, v2) => {
  if (!validator(v1) || !validator(v2)) return "Invalid Input";

  const v1Arr = v1
    .toString()
    .split(".")
    .map((item) => parseInt(item));
  const v2Arr = v2
    .toString()
    .split(".")
    .map((item) => parseInt(item));

  for (let index = 0; index < Math.max(v1Arr.length, v2Arr.length); index++) {
    const num1 = v1Arr[index] || 0;
    const num2 = v2Arr[index] || 0;
    if (num1 > num2) return v1 + " is greater than " + v2;
    if (num1 < num2) return v1 + " is smaller than " + v2;
  }
  return v1 + " is equal to " + v2;
};

console.log(compareFunction("1.0.2", "1.0.1"));
console.log(compareFunction("1", "1.0.1"));
console.log(compareFunction("1.0.2.0.4", "1.0.1"));
console.log(compareFunction("3.1.0", "1.0.1"));
console.log(compareFunction("1.0.5", "1.0.1"));
console.log(compareFunction("", "1.0.1"));

/**
 * Instructions
 *
 * Step 01: Install node in your machine.
 * Step 02: Open terminal ansd type "node question_B.js"
 */
