#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    reversedList[j] = list[i];
    j--;
  }
  return reversedList;
};
