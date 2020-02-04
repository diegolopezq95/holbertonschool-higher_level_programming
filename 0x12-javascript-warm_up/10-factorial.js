#!/usr/bin/node
function factorial (myNumber) {
  if (isNaN(myNumber) || myNumber === 1 || myNumber === 0) {
    return 1;
  } else {
    return myNumber * factorial(myNumber - 1);
  }
}
const myNumber = parseInt(process.argv[2]);
console.log(factorial(myNumber));
