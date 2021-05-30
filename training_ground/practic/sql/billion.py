import sqlite3 as sql
from time import time
from random import randint
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


con = sql.connect('test2_db.db')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 'tab1' 
                ('id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'data' INTEGER
                )
                """)
    cur.execute("""CREATE TABLE IF NOT EXISTS 'tab2' 
                ('id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'data' INTEGER
                )
                """)
    # for _ in range(1000000):
    list_numbers = '('+'),('.join([str(randint(0, 1000000))
                                   for _ in range(1000000)])+')'
    t1 = time()
    cur.execute(
        f"INSERT INTO tab1(data) VALUES {list_numbers}")
    t2 = time()
    print(f'the table1 was created in {t2 - t1} seconds')

    list_numbers = '('+'),('.join([str(randint(0, 1000000))
                                   for _ in range(1000000)])+')'
    t1 = time()
    cur.execute(
        f"INSERT INTO tab2(data) VALUES {list_numbers}")
    t2 = time()
    print(f'the table2 was created in {t2 - t1} seconds')

    t1 = time()
    cur.execute('''
            SELECT * FROM tab1, tab2 WHERE tab1.id = tab2.id
            ''')
    results = cur.fetchall()
    t2 = time()
    print(
        f'the SELECT * FROM tab1, tab2 WHERE tab1.id = tab2.id was created in {t2 - t1} seconds, lenth {len(results)}')

    t1 = time()
    cur.execute('''
            SELECT * FROM tab1 INNER JOIN  tab2
            ON tab1.id = tab2.id
            ''')
    results = cur.fetchall()
    t2 = time()
    print(
        f'the INNER JOIN was created in {t2 - t1} seconds, lenth {len(results)}')

    con.commit()
    cur.close()
