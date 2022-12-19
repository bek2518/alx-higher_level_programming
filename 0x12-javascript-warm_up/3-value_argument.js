#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  const value = process.argv[2];
  console.log(value);
}
