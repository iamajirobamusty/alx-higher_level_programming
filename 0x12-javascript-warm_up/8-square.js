#!/usr/bin/node

const { argv } = require('node:process');
let myVar = 'X';
if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing size');
} else {
  for (let itr = argv[2]; itr > 1; itr--) {
    myVar += "X";
  }
  while (argv[2]) {
    console.log(myVar);
    argv[2]--;
  }
}
