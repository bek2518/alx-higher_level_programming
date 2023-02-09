#!/usr/bin/node

const request = require('request');
const starWarsApi = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(starWarsApi + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
