#!/usr/bin/python3

'''
Script that lists all cities of a state
given as an argument from the database
'''

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states ON \
        state_id=states.id WHERE states.name LIKE BINARY (%s) \
            ORDER BY cities.id", (sys.argv[4],))
    rows = c.fetchall()
    list = ""
    for row in rows:
        for col in row:
            list += col + ", "
    print(list[:-2])
    c.close()
    db.close()
