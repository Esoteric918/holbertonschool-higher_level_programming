#!/usr/bin/node
const fs = require('fs');

require('request').get(process.argv[2], function (err, _response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
