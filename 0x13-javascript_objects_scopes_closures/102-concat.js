#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const contentfileA = fs.readFileSync(fileA);
const contentfileB = fs.readFileSync(fileB);
fs.writeFileSync(fileC, contentfileA + contentfileB);
