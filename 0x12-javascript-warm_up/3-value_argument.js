#!/usr/bin/node
let x = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  x++;
});
if (x < 3) {
  console.log('No argument');
}
