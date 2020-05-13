#!/usr/bin/node
/*
  Script that prints the number of movies where the character
  "Wedge Antilles" is present.
*/
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let index = 0; index < results.length; index++) {
      for (let char = 0; char < results[index].characters.length; char++) {
        if (results[index].characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
