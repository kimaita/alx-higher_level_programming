#!/usr/bin/node
const { readFile } = require('fs');

const filepath = process.argv[2];

readFile(filepath, 'utf-8', (err, content) => {
  if (err) console.error(err);
  else {
    console.log(content);
  }
});
