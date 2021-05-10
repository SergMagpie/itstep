import sqlite3 as sql
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

print("1 - insert\n2 - select")
choice = int(input("> "))
con = sql.connect('people.db')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'people' ('name' TEXT,
                                                      'surname' TEXT,
                                                      'city' TEXT,
                                                      'country' TEXT,
                                                      'date_of_birth' TEXT)
                """)

    if choice == 1:
        name = input("Name\n> ")
        surname = input("Surname\n> ")
        city = input("City\n> ")
        country = input("Country\n> ")
        date_of_birth = input("Date_of_birth\n> ")
        cur.execute(f"INSERT INTO 'people' VALUES ('{name}','{surname}','{city}','{country}','{date_of_birth}')")
    elif choice == 2:
        cur.execute("SELECT * FROM 'people'")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("You made a mistake")

    con.commit()
    cur.close()
