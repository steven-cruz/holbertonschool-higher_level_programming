#!/usr/bin/node
// script that prints the addition of 2 integers

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(process.argv[2], process.argv[3]);
