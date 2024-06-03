#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Not a number');
} else if (process.argv.length >= 3) {
  const argument = parseInt(process.argv[2]);
  if (argument) {
    console.log('My number: ' + argument);
  } else {
    console.log('Not a number');
  }
}
