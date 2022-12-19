#!/usr/bin/node

const argument = process.argv[2];

if (isNaN(Number(argument))) {
  console.log('Missing number of occurances');
} else {
  for (let i = 0; i < parseInt(argument); i++) {
    console.log('C is fun');
  }
}
