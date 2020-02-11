#!/usr/bin/node
const movieID = process.argv[2];
const request = require('request');
const completeUrl = `https://swapi.co/api/films/${movieID}`;
request(completeUrl, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    const filmList = JSON.parse(body).characters;
    for (const key in filmList) {
      const chars = filmList[key];
      request(chars, function (error, response, body) {
        if (error) {
          throw (error);
        } else {
          const nameList = JSON.parse(body).name;
          console.log(nameList);
        }
      });
    }
  }
});
