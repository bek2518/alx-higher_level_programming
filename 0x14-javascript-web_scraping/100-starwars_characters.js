#!/usr/bin/node

const request = require('request');
const starWarsApi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(starWarsApi, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).characters;

    for (let i = 0; i < result.length; i++) {
      console.log(result[i])
    }
  }
});
