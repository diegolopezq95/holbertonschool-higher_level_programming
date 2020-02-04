#!/usr/bin/node
let myArray = process.argv.slice(2, process.argv.length);
function sortNumber (a, b) {
  return a - b;
}
myArray = myArray.sort(sortNumber);
if (process.argv[3] === 1 || isNaN(process.argv[3])) {
  console.log('0');
} else {
  console.log(myArray[myArray.length - 2]);
}
