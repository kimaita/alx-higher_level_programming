#!/usr/bin/node
const { argv } = require('node:process');

let second = 0;

if (argv.length > 3) {
  const ints = argv.slice(2);
  ints.sort((a, b) => b - a);
  second = ints[1];
}

console.log(second);
