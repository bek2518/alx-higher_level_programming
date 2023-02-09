#!/usr/bin/node

const request = require('request');
const starWarsApi = process.argv[2];

request(starWarsApi, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < result.length; i++) {
      for (let j = 0; j < result[i].characters.length; j++) {
        const comparator = 'https://swapi-api.alx-tools.com/api/people/18/';
        if ((result[i].characters[j]) === comparator) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
