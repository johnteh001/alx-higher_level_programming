#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let ch = 0;
      while (ch < this.height) {
        let cw = 0;
        let dspl = '';
        while (cw < this.width) {
          dspl = dspl.concat(c);
          cw++;
        }
        console.log(dspl);
        ch++;
      }
    }
  }
}
module.exports = Square;
