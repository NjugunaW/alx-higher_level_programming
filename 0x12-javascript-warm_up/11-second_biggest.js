#!/usr/bin/node
const list_of_arg = process.argv;
if (list_of_arg.length <= 3) {
  console.log(0);
} else {
  console.log(list_of_arg.sort().reverse()[1]);
}