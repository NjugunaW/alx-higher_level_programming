#!/usr/bin/node
let _cnt = 0;
exports.logMe = function (item) {
  console.log(_cnt + ': ' + item);
  _cnt++;
};