#!/usr/bin/node
const movieUrl = process.argv[2];
const request = require('request');
request(movieUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body).results;
  let numMovies = 0;
  for (const movie of movies) {
    for (const chara of movie.characters) {
      if (chara.includes('18')) {
        numMovies += 1;
      }
    }
  }
  console.log(numMovies);
});
