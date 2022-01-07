#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  const newArr = arr.sort((a, b) => a - b);
  if (Math.sign(newArr[1]) === -1) {
    console.log(parseInt(newArr[1], 10));
  } else {
    newArr.reverse();
    console.log(parseInt(newArr[1], 10));
  }
}
