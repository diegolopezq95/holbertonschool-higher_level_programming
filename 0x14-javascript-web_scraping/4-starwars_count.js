#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    const resultsList = JSON.parse(body).results;
    let numFilms = 0;
    for (const key in resultsList) {
      const charactList = resultsList[key].characters;
      for (const keyj in charactList) {
        if (charactList[keyj] === 'https://swapi.co/api/people/18/' || charactList[keyj].search('18') > 0) {
          numFilms += 1;
        }
      }
    }
    console.log(numFilms);
  }
});
