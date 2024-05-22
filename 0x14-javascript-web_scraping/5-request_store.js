#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
}
);
