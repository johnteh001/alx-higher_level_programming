#!/usr/bin/node
const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');
fs.writeFile(file, str, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
