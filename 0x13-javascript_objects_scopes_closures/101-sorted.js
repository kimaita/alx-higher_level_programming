#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
