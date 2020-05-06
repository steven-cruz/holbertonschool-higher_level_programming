#!/usr/bin/node
// Script that computes and prints a factorial.

const num = Number(process.argv[2]);

function factorialize (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(num));
