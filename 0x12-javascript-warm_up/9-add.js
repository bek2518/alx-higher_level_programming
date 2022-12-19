#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  const result = Number(a) + Number(b);
  return result;
}
console.log(add(a, b));
