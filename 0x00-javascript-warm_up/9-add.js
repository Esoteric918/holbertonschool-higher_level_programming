#!/usr/bin/node


function add (a, b) {
  return a + b;
}
const a = parseInt(process.agrv[2]);
const b = parseInt(process.agrv[3]);

console.log(add(a, b));
