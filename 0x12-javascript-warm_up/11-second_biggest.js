#!/usr/bin/node
let max = -Infinity; let result = -Infinity;
let c = 2;
while (c < process.argv.length) {
  const nr = Number(process.argv[c]);
  if (nr > max) {
    result = max;
    max = nr;
  } else if (nr < max && nr > result) {
    result = nr;
  }
  c++;
}
if (process.argv.length <= 3) {
  console.log('0');
} else {
  console.log(result);
}
