#!/usr/bin/node

const argument = process.argv[2];

if (isNaN(Number(argument))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument));
}
