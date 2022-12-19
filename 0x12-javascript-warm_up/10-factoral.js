#!/usr/bin/node

function factoral (a) {
  if (isNaN(Number(a))) {
    return (1);
  }
  if (a < 1) {
    return (1);
  } else {
    return (a = a * factoral(a - 1));
  }
}
const a = process.argv[2];
const result = factoral(a);
console.log(result);
