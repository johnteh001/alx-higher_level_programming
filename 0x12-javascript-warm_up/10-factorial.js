#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || (n === 0) || (n === 1)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const argument = parseInt(process.argv[2]);
const result = factorial(argument);
console.log(result);
