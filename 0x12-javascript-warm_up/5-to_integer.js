#!/usr/bin/node
const { argv } = require('node:process');

const arg = parseInt(argv[2]);

console.log(isNaN(arg) ? 'Not a number' : `My number: ${arg}`);
