#!/usr/bin/node
const file_1 = process.argv[2];
const file_2 = process.argv[3];
const res_ult = process.argv[4];
const file = require('fs');
const file_txt1 = file.readFileSync(file_1);
const file_txt2 = file.readFileSync(file_2);
file.writeFileSync(res_ult, file_txt1 + file_txt2);