#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    const allList = JSON.parse(body);
    const myDict = {};
    for (const key in allList) {
      if (allList[key].completed) {
        if (!(allList[key].userId in myDict)) {
          myDict[allList[key].userId] = 1;
        } else {
          myDict[allList[key].userId]++;
        }
      }
    }
    console.log(myDict);
  }
});
