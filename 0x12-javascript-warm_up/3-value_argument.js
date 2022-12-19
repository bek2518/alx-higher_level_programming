#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const value = process.argv[2];
  console.log(value);
}
