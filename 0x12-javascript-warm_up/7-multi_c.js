#!/usr/bin/node
const { argv } = require('node:process');

let x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
