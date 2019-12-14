#!/usr/bin/python3
""" This module takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    users = sys.argv[1]
    password = sys.argv[2]
    datab = sys.argv[3]
    record = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=users,
                         passwd=password, db=datab, charset="utf8")
    """ create an instance of 'cursor' class
    used to execute the 'SQL' statements in 'Python'
    """
    cursor = db.cursor()
    """ getting records from the table
    """
    cursor.execute("SELECT cities.name FROM cities\
                   INNER JOIN states ON states.id = cities.state_id\
                   WHERE states.name LIKE BINARY %s\
                   ORDER BY cities.id ASC", (record,))
    """ fetching all records from the 'cursor' object
    """
    records = cursor.fetchall()
    """ showing the data
    """
    for row in range(len(records)):
        args = ''.join(records[row])
        if row != len(records) - 1:
            print("{}".format(args), end=", ")
        else:
            print("{}".format(args))
    cursor.close()
    db.close()
