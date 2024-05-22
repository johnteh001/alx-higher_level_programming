#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(body);
  const dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };
  for (const task of tasks) {
    if (task.completed === true) {
      dict[task.userId]++;
    }
  }
  for (const key in dict) {
    const vari = dict[key];
    if (vari === 0) {
      delete dict[key];
    }
  }
  console.log(dict);
});
