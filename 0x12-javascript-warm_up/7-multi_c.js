#!/usr/bin/node
// script that prints x times C is fun.
let x = process.argv[2];
let count = 0;

if (isNaN(process.argv[2])) {
  console.log("Missing number of occurrences");
}

for (count = 0; count < x; count++) {
  console.log('C is fun');
}
