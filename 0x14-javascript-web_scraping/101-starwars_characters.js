#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.log('Usage: ./101-starwars_characters.js <movie_id>');
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
        return;
    }

    const characterUrls = body.characters;

    characterUrls.forEach((characterUrl) => {
        request(characterUrl, { json: true }, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }
            if (response.statusCode !== 200) {
                console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
                return;
            }

            console.log(body.name);
        });
    });
});

