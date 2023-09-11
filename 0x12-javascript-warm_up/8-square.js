#!/usr/bin/node
const digit = process.argv[2];
if (!parseInt(digit)) {
  console.log('Missing size');
} else {
  for (let ab = 0; ab < digit; ab++) {
    console.log('X'.repeat(digit));
  }
}