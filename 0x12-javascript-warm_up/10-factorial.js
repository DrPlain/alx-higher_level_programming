#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
