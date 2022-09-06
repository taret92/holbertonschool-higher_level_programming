#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states on \
                            cities.state_id = states.id\
                                ORDER BY cities.id")
    result = cursor.fetchall()
    for value in result:
        print(value)
