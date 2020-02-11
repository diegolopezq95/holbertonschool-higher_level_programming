#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) throw err;
    });
  }
});
