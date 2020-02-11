#!/usr/bin/node
const episodeID = process.argv[2];
const completeUrl = `http://swapi.co/api/films/${episodeID}`;
const request = require('request');
request(completeUrl, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
