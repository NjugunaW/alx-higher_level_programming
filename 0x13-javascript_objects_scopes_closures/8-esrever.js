#!/usr/bin/node
exports.esrever = function (list) {
    const lst_nw = [];
    for (let ax = 0; ax < list.length; ax++) {
      lst_nw.unshift(list[ax]);
    }
    return lst_nw;
  };