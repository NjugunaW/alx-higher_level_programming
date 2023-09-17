#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let cnt = 0;
    for (const ax in list) {
      if (list[ax] === searchElement) {
        cnt++;
      }
    }
    return cnt;
  };