#!/usr/bin/node
const request = require('request');

const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) console.error(error);
  if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let filmCount = 0;
    for (const film of films.results) {
      for (const char of film.characters) {
        if (char.split('/').includes('18')) filmCount++;
      }
    }
    console.log(filmCount);
  }
});
