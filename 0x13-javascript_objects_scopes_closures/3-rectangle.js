#!/usr/bin/node
// create an instance method calle print()

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.heigth = h;
    }
  }

  print () {
    for (let count = 0; count < this.heigth; count++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
