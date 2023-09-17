#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    user_name = args[1]
    pass_word = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=user_name,
                         passwd=pass_word, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute('SELECT * FROM states ORDER BY states.id;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()