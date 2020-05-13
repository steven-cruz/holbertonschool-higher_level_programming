#!/usr/bin/node
// Script that computes the numer of tasks completed by user id.
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    const dict = {};
    for (let idx = 0; idx < result.length; idx++) {
      if (result[idx].completed === true) {
        if (dict[result[idx].userId] === undefined) {
          dict[result[idx].userId] = 1;
        } else {
          dict[result[idx].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
