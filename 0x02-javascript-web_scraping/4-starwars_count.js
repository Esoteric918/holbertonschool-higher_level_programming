#!/usr/bin/node

const request = require('request');
const starWars = process.argv[2];
request(starWars, function (_err, res, body) {
  let count = 0;
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; ++i) {
    for (let x = 0; x < data[i].characters.length; ++x) {
      if (data[i].characters[x] === '18') {
      }
      count++;
    }
  }
  console.log(count);
});
