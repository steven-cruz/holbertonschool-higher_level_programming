#!/usr/bin/node
// if w or h is equal to 0 or not a posivite integer, create an empty object.

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
