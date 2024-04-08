#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing size');
} else if (process.argv.length >= 3) {
  const argument = parseInt(process.argv[2]);
  if (Number.isNaN(argument)) {
    console.log('Missing size');
  }
  let count = 0;
  while (count < argument) {
    let kount = 0;
    let displ = '';
    while (kount < argument) {
      displ = displ.concat('X');
      kount++;
    }
    console.log(displ);
    count++;
  }
}
