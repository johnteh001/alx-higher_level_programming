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
}
module.exports = Rectangle;
