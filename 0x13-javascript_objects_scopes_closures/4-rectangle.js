#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ch = 0;
    while (ch < this.height) {
      let cw = 0;
      let dspl = '';
      while (cw < this.width) {
        dspl = dspl.concat('X');
        cw++;
      }
      console.log(dspl);
      ch++;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
