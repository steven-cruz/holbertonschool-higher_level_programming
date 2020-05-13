#!/usr/bin/node
// Script that gets the contents of a webpage and sotre ir in a fil
const request = require('request');
const fs = require('fs');
request(process.argv[2], 'utf8').pipe(fs.createWriteStream(process.argv[3]));
