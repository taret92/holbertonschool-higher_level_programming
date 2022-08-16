#!/usr/bin/node
const process = require('process');
const args = process.argv;
const limit = parseInt(args[2]);
const string = 'C is fun';
if (limit) {
  for (let i = 0; i < limit; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
