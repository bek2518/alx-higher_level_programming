#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else if (process.argv.length > 3) {
  let biggest;
  let secondBiggest;

  if (process.argv[2] < process.argv[3]) {
    biggest = process.argv[3];
    secondBiggest = process.argv[2];
  } else {
    biggest = process.argv[2];
    secondBiggest = process.argv[3];
  }

  if (process.argv.length > 4){
    for (let i = 4; i < process.argv.length; i++) {
      if (biggest > process.argv[i]) {
        if (secondBiggest > process.argv[i]) {
          biggest = biggest;
          secondBiggest = secondBiggest;
        } else {
          biggest = biggest;
          secondBiggest = process.argv[i];
        }
      }
      else {
        if (secondBiggest > process.argv[i]) {
          biggest = process.argv[i];
          secondBiggest = secondBiggest;
        } else {
          biggest = process.argv[i];
          secondBiggest = process.argv[i];
        }
      }
    }
  }
  console.log(secondBiggest);
}
