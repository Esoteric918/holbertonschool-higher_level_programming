#!/usr/bin/node
const request = require('request');
const starWars = 'https://swapi-api.hbtn.io/api/films/' + (process.argv[2]);

request(starWars, (_err, _res, body) => {
  const thing = JSON.parse(body);
  console.log(thing.title);
});
