#!/usr/bin/node
/*
* Write a script that prints a square.
* variable x contains the number of characters to print.
*/

const x = process.argv[2];
let count = 0;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (count = 0; count < x; count++) {
  console.log('X'.repeat(x));
}
