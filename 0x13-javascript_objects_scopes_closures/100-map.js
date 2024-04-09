#!/usr/bin/node
const origList = require('./100-data').list;

const modList = origList.map((elem, i) => elem * i);

console.log(modList);
