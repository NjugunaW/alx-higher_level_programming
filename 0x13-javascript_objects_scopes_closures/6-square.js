#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
    charPrint (c) {
      if (c === 'X') {
        this.print();
      } else {
        for (let ax = 0; ax < this.height; ax++) console.log(c.repeat(this.width));
      }
    }
  };