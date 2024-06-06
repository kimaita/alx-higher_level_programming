#!/usr/bin/node
/**
 * Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
 */

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(endpoint, { json: true }, (error, response, film) => {
  if (error) {
    console.error(error);
  } else {
    const promises = Array.from(
      film.characters,
      (character) =>
        new Promise((resolve, reject) => {
          request.get(character, { json: true }, (err, resp, actor) => {
            if (err) {
              console.error(err);
            } else {
              resolve(actor.name);
            }
          });
        })
    );

    Promise.all(promises).then((actorNames) => {
      actorNames.forEach((entry) => {
        console.log(entry);
      });
    });
  }
});
