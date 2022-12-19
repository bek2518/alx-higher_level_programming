#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else if (process.argv.length > 3) {
  let biggest;
  let secondBiggest;

  if (Number(process.argv[2]) < Number(process.argv[3])) {
    biggest = Number(process.argv[3]);
    secondBiggest = Number(process.argv[2]);
  } else {
    biggest = Number(process.argv[2]);
    secondBiggest = Number(process.argv[3]);
  }

  if (process.argv.length > 4) {
    for (let i = 4; i < process.argv.length; i++) {
      if (biggest > process.argv[i]) {
        if (secondBiggest < Number(process.argv[i])) {
          secondBiggest = Number(process.argv[i]);
        }
      } else {
        secondBiggest = biggest;
        biggest = Number(process.argv[i]);
      }
    }
  }
  console.log(secondBiggest);
}
