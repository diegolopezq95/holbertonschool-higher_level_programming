#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function myConverter (number) {
    return number.toString(this.base);
  }
  return myConverter;
};
