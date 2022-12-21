#!/usr/bin/python3

'''
Script that lists all cities from the database
'''

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON state_id=states.id ORDER BY cities.id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
