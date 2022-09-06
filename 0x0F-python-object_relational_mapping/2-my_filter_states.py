#!/usr/bin/python3
"""script that lists all states from
the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """main function"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name='{}'
         ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        if (state[1] == sys.argv[4]):
            print(state)

    cur.close()
    db.close()
