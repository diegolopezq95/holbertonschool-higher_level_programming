#!/usr/bin/python3
""" This module ists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    users = sys.argv[1]
    password = sys.argv[2]
    datab = sys.argv[3]
    db = MySQLdb.connect(host = "localhost", port = 3307, user = users,
                         passwd = password, db = datab, charset = "utf8")
""" create an instance of 'cursor' class, used to execute the 'SQL' statements in 'Python'
"""
cursor = db.cursor()
""" getting records from the table
"""
cursor.execute("SELECT * FROM states ORDER BY id ASC")
""" fetching all records from the 'cursor' object
"""
records = cursor.fetchall()
""" showing the data
""" 
for row in records:
    print(row)
cursor.close()
db.close()
