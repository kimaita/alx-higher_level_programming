#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return (a + b);
}

const intA = parseInt(argv[2]);
const intB = parseInt(argv[3]);

console.log(add(intA, intB));
