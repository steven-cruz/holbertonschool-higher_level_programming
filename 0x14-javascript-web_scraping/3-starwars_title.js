#!/usr/bin/node
/*
  Script that prints the numer of movies where the charater
  "Wedge antilles" is present.
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
