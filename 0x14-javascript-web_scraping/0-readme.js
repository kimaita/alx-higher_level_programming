#!/usr/bin/node
const { readFile } = require('fs');

const filepath = process.argv[2];

readFile(filepath, 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
