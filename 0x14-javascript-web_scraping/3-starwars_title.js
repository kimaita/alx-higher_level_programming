#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) console.error(error);
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
