#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorail (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  } else {
    return num * factorail(num - 1);
  }
}

console.log(factorail(num));
