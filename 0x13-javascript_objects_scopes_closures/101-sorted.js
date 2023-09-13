#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const _user_Id in dict) {
  if (newDict[dict[_user_Id]] === undefined) {
    newDict[dict[_user_Id]] = [_user_Id];
  } else {
    newDict[dict[_user_Id]].push(_user_Id);
  }
}
console.log(newDict);