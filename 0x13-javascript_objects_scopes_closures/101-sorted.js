#!/usr/bin/node
const valueValues = require('./101-data.js').dict;
const dictOrder = {};
for (const key in valueValues) {
  if (!(valueValues[key] in dictOrder)) {
    dictOrder[valueValues[key]] = [];
    dictOrder[valueValues[key]].push(key);
  } else {
    dictOrder[valueValues[key]].push(key);
  }
}
console.log(dictOrder);
