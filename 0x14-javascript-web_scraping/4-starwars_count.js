#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const resultsList = JSON.parse(body).results;
    let numFilms = 0;
    for (const key in resultsList) {
      const charactList = resultsList[key].characters;
      for (const keyj in charactList) {
        if (charactList[keyj] === 'https://swapi.co/api/people/18/') {
          numFilms += 1;
        }
      }
    }
    console.log(numFilms);
  }
});
