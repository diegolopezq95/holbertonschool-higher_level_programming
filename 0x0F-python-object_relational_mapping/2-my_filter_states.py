#!/usr/bin/python3
""" This module takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
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
cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
               .format(record))
""" fetching all records from the 'cursor' object
"""
records = cursor.fetchall()
""" showing the data
"""
for row in records:
    print(row)
cursor.close()
db.close()
