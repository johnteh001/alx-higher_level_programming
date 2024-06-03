#!/usr/bin/env node

const request = require('request');

if (process.argv.length < 3) {
    console.log('Usage: ./100-starwars_characters.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];
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
