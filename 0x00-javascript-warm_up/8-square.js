#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  for (let x = 0; x < num; ++x) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
