#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
    }
    print () {
      for (let ax = 0; ax < this.height; ax++) console.log('X'.repeat(this.width));
    }
  };
