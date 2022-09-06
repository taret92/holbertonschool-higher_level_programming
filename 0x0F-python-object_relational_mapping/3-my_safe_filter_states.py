#!/usr/bin/python3
"""script that lists all states from
the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                        ORDER BY id ASC", (argv[4], ))
    result = mycursor.fetchall()
    for result in result:
        print(result)
    mycursor.close()
    database.close()
