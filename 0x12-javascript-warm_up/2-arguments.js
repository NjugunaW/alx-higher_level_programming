#!/usr/bin/node
const arg_count = process.argv.length;
if (arg_count > 2) {
  console.log('Arguments found');
} else if (arg_count === 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}