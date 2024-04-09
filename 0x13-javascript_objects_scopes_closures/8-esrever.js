#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  while (list.length) {
    revlist.push(list.pop());
  }
  return revlist;
};
