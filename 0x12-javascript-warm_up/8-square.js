#!/usr/bin/node

const argument = process.argv[2];

if (isNaN(Number(argument))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argument); i++) {
    console.log('X'.repeat(argument));
  }
}
