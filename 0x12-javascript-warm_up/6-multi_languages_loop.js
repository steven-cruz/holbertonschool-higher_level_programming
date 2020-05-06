#!/usr/bin/node
/*
* Script that prints 3 lines but by using an array of string and a loop.
*/

const cont = ['C is fun', 'Python is cool', 'Javascript is amazing'];
const len = cont.length;
let runs = 0;

for (runs = 0; runs < len; runs++) {
  console.log(cont[runs]);
}
