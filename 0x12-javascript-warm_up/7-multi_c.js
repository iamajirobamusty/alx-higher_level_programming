#!/usr/bin/node

const { argv } = require('node:process');
if (!argv[2]) {
  console.log('Missing number of occurences');
} else {
  while (argv[2] > 0) {
    console.log('C is fun');
    argv[2] = argv[2] - 1;
  }
}
