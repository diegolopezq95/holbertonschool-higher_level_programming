#!/usr/bin/node
const dict = require('./101-data.js');
const dictValues = Object.values(dict);
const valueValues = dictValues[0];
const dictOrder = {};
for (let key in valueValues) {
  if (!(valueValues[key] in dictOrder)) {
    dictOrder[valueValues[key]] = [];
    dictOrder[valueValues[key]].push(key);
  } else {
    dictOrder[valueValues[key]].push(key);
  }
}
console.log(dictOrder);
