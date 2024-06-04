#!/usr/bin/node
const { writeFile } = require('fs');

const filepath = process.argv[2];
const content = process.argv[3];

writeFile(filepath, content, (err) => {
  if (err) console.error(err);
});
