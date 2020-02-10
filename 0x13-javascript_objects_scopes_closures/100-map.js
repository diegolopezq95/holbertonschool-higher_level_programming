#!/usr/bin/node
const list = require('./100-data.js').list;
const newlist = list.map(function (number, index) {
  return (number * index);
});
console.log(list);
console.log(newlist);
