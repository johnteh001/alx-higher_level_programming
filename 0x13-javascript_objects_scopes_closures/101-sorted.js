#!/usr/bin/node
const di = require('./101-data').dict;
const obj = {};
for (const [key, value] of Object.entries(di)) {
  if (obj[value] === undefined) {
    obj[value] = [key];
  } else {
    obj[value].push(key);
  }
}
console.log(obj);
