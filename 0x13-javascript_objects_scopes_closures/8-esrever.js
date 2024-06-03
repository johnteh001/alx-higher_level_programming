#!/usr/bin/node
exports.esrever = function (list) {
  const listrev = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    listrev.push(list[i]);
  }
  return listrev;
};
