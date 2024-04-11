#!/usr/bin/python3
"""Script takes in the name of state and list all cities"""

import MySQLdb
import sys
if __name__ == "__main__":
    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=user_name, passwd=pass_word, db=database,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %(state)s
            ORDER BY cities.id ASC""", {'state': state})
    rows = c.fetchall()
    lis = []
    for r in rows:
        lis.append(r[0])
    final = ", ".join(lis)
    print(final)

    c.close()
    db.close()
