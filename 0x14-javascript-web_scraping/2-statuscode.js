#!/usr/bin/node
// Script that display the statud code of a GET request.
const request = require('request');
request(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
