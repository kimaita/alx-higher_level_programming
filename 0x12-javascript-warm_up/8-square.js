#!/usr/bin/node
const { argv } = require('node:process');

const arg = parseInt(argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let x = arg;
  while (x > 0) {
    console.log('X'.repeat(arg));
    x--;
  }
}
