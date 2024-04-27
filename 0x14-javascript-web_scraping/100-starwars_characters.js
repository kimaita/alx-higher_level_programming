#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) console.error(error);
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    for (const char of film.characters) {
      getCharacter(char);
    }
  }
});

function getCharacter (url) {
  request(url, function (error, response, body) {
    if (error) console.error(error);
    if (response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
    }
  });
}
