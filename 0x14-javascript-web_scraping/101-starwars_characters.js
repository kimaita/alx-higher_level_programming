#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(endpoint, { json: true }, function (error, response, film) {
  if (error) console.error(error);
  if (response.statusCode === 200) {
    const characters = Object.fromEntries(
      film.characters.map((char) => [char, ''])
    );
    setCharacters(characters);
  }
});

function setCharacters (characters) {
  for (const url of Object.keys(characters)) {
    request.get(url, { json: true }, (error, response, character) => {
      if (error) console.error(error);

      if (response.statusCode === 200) characters[url] = character.name;

      if (Object.values(characters).every((x) => x)) {
        for (const char of Object.values(characters)) {
          console.log(char);
        }
      }
    });
  }
}
