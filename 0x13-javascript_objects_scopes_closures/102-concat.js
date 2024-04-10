#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
fs.readFile(file1, (err, data) => {
  if (err) throw err;
  fs.appendFile(file3, data, function (err) {
    if (err) throw err;
  });
});
fs.readFile(file2, (err, dat) => {
  if (err) throw err;
  fs.appendFile(file3, dat, function (err) {
    if (err) throw err;
  });
});
