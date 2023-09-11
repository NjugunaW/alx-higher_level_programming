#!/usr/bin/node
if (process.argv[2]) {
    for (let ab = 0; ab < process.argv[2]; ab++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }