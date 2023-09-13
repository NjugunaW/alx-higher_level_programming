#!/usr/bin/node
const _arr_lst = require('./100-data.js').list;

const lst_nw = _arr_lst.map((k, index) => k * index);
console.log(_arr_lst);
console.log(lst_nw);