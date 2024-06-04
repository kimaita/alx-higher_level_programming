#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(endpoint, (err, resp, body) => {
  if (resp.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  }
  if (err) {
    console.error(err);
  }
});
