#!/usr/bin/node

let argument = process.argv[2];

if ((function () { argument = Number(argument); } === undefined) || process.argv.length < 3) {
  console.log('Not a number');
} else {
  console.log(argument);
}
