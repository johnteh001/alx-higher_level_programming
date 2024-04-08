#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else if (process.argv.length >= 3) {
  const argument = parseInt(process.argv[2]);
  let count = 0;
  while (count < argument) {
    console.log('C is fun');
    count++;
  }
}
