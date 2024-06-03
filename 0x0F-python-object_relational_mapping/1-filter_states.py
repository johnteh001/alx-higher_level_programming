#!/usr/bin/python3
"""Script list all States with name starting with N"""

import MySQLdb
import sys
if __name__ == "__main__":
    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=user_name, passwd=pass_word, db=database,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE BINARY states.name LIKE 'N%'
            ORDER BY states.id ASC""")
    rows = c.fetchall()
    for r in rows:
        print(r)

    c.close()
    db.close()
