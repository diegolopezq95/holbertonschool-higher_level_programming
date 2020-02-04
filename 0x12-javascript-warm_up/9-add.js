#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
} console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
