#!/usr/bin/python3

'''
Script that lists all states from the database
matching the argument name passed
'''

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}' \
        ORDER BY states.id".format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
