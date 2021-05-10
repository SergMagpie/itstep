import sqlite3 as sql
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def display_of_all_people():
    cur.execute("SELECT * FROM people")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def display_people_with_age_in_the_range():
    cur.execute("SELECT name, date_of_birth FROM people")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def displaying_all_people_from_one_city():
    what_city = input('What city? ')
    cur.execute(f"SELECT * FROM people WHERE city LIKE '{what_city}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    pass

print("1 - insert\n2 - all_people\n3 - people_with_age\n4 - people_from_one_city")
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
        cur.execute(
            f"INSERT INTO 'people' VALUES ('{name}','{surname}','{city}','{country}','{date_of_birth}')")
    elif choice == 2:
        display_of_all_people()
        # cur.execute("SELECT * FROM 'people'")
        # rows = cur.fetchall()
        # for row in rows:
        #     print(row)
    elif choice == 3:
        display_people_with_age_in_the_range()

    elif choice == 4:
        displaying_all_people_from_one_city()
    else:
        print("You made a mistake")





    # displaying_all_people_from_one_countries(set as a parameter by the user
    #                                          from the keyboard)

    con.commit()
    cur.close()
