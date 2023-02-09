#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = {};

    for (let i = 1; i <= 10; i++) {
      let counter = 0;
      for (let j = 0; j < JSON.parse(body).length; j++) {
        const userId = JSON.parse(body)[j].userId;
        const completed = JSON.parse(body)[j].completed;

        if (userId === i && completed === true) {
          counter++;
        }
      }
      result[i] = counter;
    }
    console.log(result);
  }
});
