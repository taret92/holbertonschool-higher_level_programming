#!/usr/bin/python3
"""script that lists all states from
the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    """main function"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                        ORDER BY id ASC", (argv[4], ))
    states = cur.fetchall()

    for state in states:
        print(state)
