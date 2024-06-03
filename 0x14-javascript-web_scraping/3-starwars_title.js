#!/usr/bin/node
const movieId = '' + process.argv[2];
const movieUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');
request(movieUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
