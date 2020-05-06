#!/usr/bin/node
/*
* script that prints My number: <first argument converted in integer>
* If the argument cant be converted to an integer, print Not a number.
*/
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2], 10));
}
