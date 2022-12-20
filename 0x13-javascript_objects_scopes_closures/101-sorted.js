#!/usr/bin/node

const dict = require('./101-data').dict;

const dictionary = {};
for (const key in dict) {
  if (dictionary[dict[key]] === undefined) {
    dictionary[dict[key]] = [];
  }
  dictionary[dict[key]].push(key);
}
console.log(dictionary);
