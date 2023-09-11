#!/usr/bin/node
const int = parseInt(process.argv[2]);
if (int) {
  console.log('My number: ' + int);
} else {
  console.log('Not a number');
}