#!/usr/bin/python3
#  takes in the name of a state as an argument and lists all cities
#  of that state.

import MySQLdb


from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id \
    = states.id WHERE states.name LIKE %s ORDER BY cities.id ASC", (argv[4],))
    print(", ".join(rows[0] for rows in c.fetchall()))

    c.close()
    db.close()
