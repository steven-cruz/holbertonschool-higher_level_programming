#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const list = [];
let count = 2;
const arg = process.argv.length;

if (process.argv.length < 4) {
  console.log(0);
} else {
  for (count = 2; count < arg; count++) {
    list.push(Number(process.argv[count]));
  }
  console.log(list.sort()[list.length - 2]);
}
