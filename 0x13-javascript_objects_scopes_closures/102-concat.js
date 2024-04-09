#!/usr/bin/node
const fs = require('node:fs');

try {
  const file1 = fs.readFileSync(process.argv[2], 'utf8');
  const file2 = fs.readFileSync(process.argv[3], 'utf8');
  const combined = file1.concat(file2);
  fs.writeFileSync(process.argv[4], combined);
} catch (err) {
  console.error(err);
}
