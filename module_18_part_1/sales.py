import sqlite3 as sql
import os
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
file_name = "names.json"
file_invoice = "invoice.json"


def select_for_select():
    menu = {
        '1': ('1 - Display of all transactions',
              display_of_all_transactions),
        '2': ('2 - Display of all sellers',
              display_of_all_sellers),
        '3': ('3 - Display of all buyers',
              display_of_all_buyers),
        '4': ('4 - Display of transactions of a specific seller',
              display_of_transactions_of_a_specific_seller),
        '5': ('5 - Display of the maximum transaction amount',
              display_of_the_maximum_transaction_amount),
        '6': ('6 - Display of the minimum transaction amount',
              display_of_the_minimum_transaction_amount),
        '7': ('7 - Display the maximum transaction amount for specific seller',
              display_the_maximum_transaction_amount_for_specific_seller),
        '8': ('8 - Display the minimum transaction amount for specific seller',
              display_the_minimum_transaction_amount_for_specific_seller),
        '9': ('9 - Display the maximum transaction amount for specific buyer',
              display_the_maximum_transaction_amount_for_specific_buyer),
        '10': ('10 - Display the minimum transaction amount for specific buyer',
               display_the_minimum_transaction_amount_for_specific_buyer),
        '11': ('11 - Display the seller who has the maximum the amount of sales for all transactions',
               display_the_seller_who_has_the_maximum_the_amount_of_sales_for_all_transactions),
        '12': ('12 - Display of the buyer who has the maximum the amount of purchases on all transactions',
               display_of_the_buyer_who_has_the_maximum_the_amount_of_purchases_on_all_transactions),
    }
    key = None
    while key != 'exit':
        for i in menu:
            print(menu[i][0])
        print('exit for exit')
        key = input("> ")
        if key in menu:
            menu[key][1]()
        elif key == 'exit':
            break
        else:
            print('You made a mistake')


def display_of_all_transactions():
    cur.execute("""
                SELECT
                    sales.invoice, 
                    salesmen.name || ' ' || salesmen.surname AS seller,
                    customers.name || ' ' || customers.surname AS buyer,
                    sales.date,
                    sales.goods,
                    sales.amount,
                    sales.price
                FROM
                    sales
                INNER JOIN salesmen ON
                    sales.seller_id = salesmen.seller_id
                INNER JOIN customers ON
                    sales.customer_id = customers.customer_id    
                """)
    rows = cur.fetchall()
    print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))


def display_of_all_sellers():
    cur.execute("SELECT * FROM salesmen")
    rows = cur.fetchall()
    print("{:<10}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        print("{:<10}{:<10}{:<10}".format(*row))
    


def display_of_all_buyers():
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    print("{:<10}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        print("{:<10}{:<10}{:<10}".format(*row))
   


def display_of_transactions_of_a_specific_seller():
    pass


def display_of_the_maximum_transaction_amount():
    cur.execute("""
                SELECT
                    sales.invoice, 
                    salesmen.name || ' ' || salesmen.surname AS seller,
                    customers.name || ' ' || customers.surname AS buyer,
                    sales.date,
                    sales.goods,
                    sales.amount,
                    MAX(sales.price)
                FROM
                    sales
                INNER JOIN salesmen ON
                    sales.seller_id = salesmen.seller_id
                INNER JOIN customers ON
                    sales.customer_id = customers.customer_id    
                """)
    rows = cur.fetchall()
    print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))


def display_of_the_minimum_transaction_amount():
    cur.execute("""
                SELECT
                    sales.invoice, 
                    salesmen.name || ' ' || salesmen.surname AS seller,
                    customers.name || ' ' || customers.surname AS buyer,
                    sales.date,
                    sales.goods,
                    sales.amount,
                    MIN(sales.price)
                FROM
                    sales
                INNER JOIN salesmen ON
                    sales.seller_id = salesmen.seller_id
                INNER JOIN customers ON
                    sales.customer_id = customers.customer_id    
                """)
    rows = cur.fetchall()
    print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        print("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))


def display_the_maximum_transaction_amount_for_specific_seller():
    pass


def display_the_minimum_transaction_amount_for_specific_seller():
    pass


def display_the_maximum_transaction_amount_for_specific_buyer():
    pass


def display_the_minimum_transaction_amount_for_specific_buyer():
    pass


def display_the_seller_who_has_the_maximum_the_amount_of_sales_for_all_transactions():
    pass


def display_of_the_buyer_who_has_the_maximum_the_amount_of_purchases_on_all_transactions():
    pass

# def display_of_all_people():
#     cur.execute("SELECT * FROM people")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# def display_people_with_age_in_the_range():
#     cur.execute("SELECT name, date_of_birth FROM people")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)


# def displaying_all_people_from_one_city():
#     what_city = input('What city? ')
#     cur.execute(f"SELECT * FROM people WHERE city LIKE '{what_city}'")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     pass
con = sql.connect('sales.db')
with con:
    cur = con.cursor()
    cur.execute("""PRAGMA foreign_keys=on;""")
    cur.execute("""                
                CREATE TABLE IF NOT EXISTS sales (
                'invoice' INTEGER PRIMARY KEY AUTOINCREMENT,
                'seller_id' INTEGER NOT NULL,
                'customer_id' INTEGER NOT NULL,
                'date' TEXT NOT NULL,
                'goods' TEXT NOT NULL,
                'amount' INTEGER NOT NULL,
                'price' DECIMAL (10, 2) NOT NULL,
                FOREIGN KEY (seller_id) 
                    REFERENCES "salesmen" (seller_id)
                        ON UPDATE RESTRICT
                        ON DELETE RESTRICT,
                FOREIGN KEY (customer_id) 
                    REFERENCES "customers" (customer_id))                        
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS 'salesmen' 
                ('seller_id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'name' TEXT NOT NULL,
                'surname' TEXT NOT NULL)
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS 'customers' 
                ('customer_id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'name' TEXT NOT NULL,
                'surname' TEXT NOT NULL)
                """)
    if input('Create base? y/n ') == 'y':
        try:
            for table_name in 'salesmen', 'customers':
                with open(file_name, "r") as f:
                    json_data = json.load(f)
                    for i, j in json_data:
                        cur.execute(f"""
                                    INSERT INTO {table_name} 
                                    VALUES(NULL, '{i}', '{j}')
                                    """)
            with open(file_invoice, "r") as f:
                json_data = json.load(f)
                for i in json_data:
                    cur.execute("""
                                INSERT INTO sales 
                                VALUES(NULL, '{}','{}',
                                '{}','{}','{}','{}')
                                """.format(*i))
        except FileNotFoundError:
            print('The file is damaged. Base is empty.')


choice = None
while choice != 'exit':
    print("1 - SELECT\n2 - INSERT\n3 - UPDATE\n4 - DELETE\nexit for exit")
    choice = input("> ")
    if choice == '1':  # SELECT
        select_for_select()

    elif choice == '2':  # INSERT
        pass
    elif choice == '3':  # UPDATE
        pass
    #     display_people_with_age_in_the_range()

    elif choice == '4':  # DELETE
        pass

    else:
        print('You made a mistake')
print('Goodbye!')
con.commit()
cur.close()
