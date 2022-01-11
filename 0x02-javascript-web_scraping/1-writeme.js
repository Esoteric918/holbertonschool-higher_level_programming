#!/usr/bin/node
let fs = require('fs')
let data = process.argv[3]
fs.writeFile(process.argv[2], data, 'utf-8',  (err) => {
  if (err){
    console.log(err);
  }
});
