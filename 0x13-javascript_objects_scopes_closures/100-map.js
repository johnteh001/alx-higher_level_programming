#!/usr/bin/node
const arglist = require('./100-data').list;
const newList = arglist.map((x, y) => x * y);
console.log(arglist);
console.log(newList);
