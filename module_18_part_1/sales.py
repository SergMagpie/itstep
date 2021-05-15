import sqlite3 as sql
import os
import json
import re

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
file_name = "names.json"
file_invoice = "invoice.json"

def write_to_file(message, filename="output.txt"):
    """
    Function for write output data.
    """    
    with open(filename, "a") as f:
        for string in message:
            f.write(string + '\n') 
        f.write('\n') 


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
    while key != '0':
        for i in menu:
            print(menu[i][0])
        print('0 for exit to main menu')
        key = input("> ")
        if key in menu:
            menu[key][1]()
        elif key == '0':
            break
        else:
            print('You made a mistake')


def display_of_all_transactions():  # 1
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
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)

def display_of_all_sellers():  # 2
    cur.execute("SELECT * FROM salesmen")
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)

def display_of_all_buyers():  # 3
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_of_transactions_of_a_specific_seller():  # 4
    print("Please, enter seller's name")
    seller_name = input('> ')
    cur.execute(f"""
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
                WHERE seller = "{seller_name}"
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_of_the_maximum_transaction_amount():  # 5
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
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_of_the_minimum_transaction_amount():  # 6
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
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_the_maximum_transaction_amount_for_specific_seller():  # 7
    print("Please enter the name of the seller whose maximum deal you want to see")
    seller_name = input('> ')
    cur.execute(f"""
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
                WHERE seller = "{seller_name}"
                ORDER BY sales.price * sales.amount DESC
                LIMIT 1
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)



def display_the_minimum_transaction_amount_for_specific_seller():  # 8
    print("Please enter the name of the seller whose minimum deal you want to see")
    seller_name = input('> ')
    cur.execute(f"""
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
                WHERE seller = "{seller_name}"
                ORDER BY sales.price * sales.amount ASC
                LIMIT 1
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_the_maximum_transaction_amount_for_specific_buyer():  # 9
    print("Please enter the name of the buyer whose maximum deal you want to see")
    buyer_name = input('> ')
    cur.execute(f"""
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
                WHERE buyer = "{buyer_name}"
                ORDER BY sales.price * sales.amount DESC
                LIMIT 1
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_the_minimum_transaction_amount_for_specific_buyer():  # 10
    print("Please enter the name of the buyer whose minimum deal you want to see")
    buyer_name = input('> ')
    cur.execute(f"""
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
                WHERE buyer = "{buyer_name}"
                ORDER BY sales.price * sales.amount ASC
                LIMIT 1
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<10}{:<25}{:<25}{:<15}{:<25}{:<10}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_the_seller_who_has_the_maximum_the_amount_of_sales_for_all_transactions():  # 11
    cur.execute("""
                SELECT
                    salesmen.name || ' ' || salesmen.surname AS seller,
                    SUM(sales.amount * sales.price) AS total_value                    
                FROM
                    sales                    
                INNER JOIN salesmen ON
                    sales.seller_id = salesmen.seller_id                
                GROUP BY seller
                HAVING total_value = 
                                    (SELECT MAX(summ) 
                                    FROM
                                        (SELECT                                       
                                            SUM(amount * price) AS summ
                                        FROM
                                            sales                                       
                                        GROUP BY seller_id))
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<25}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<25}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def display_of_the_buyer_who_has_the_maximum_the_amount_of_purchases_on_all_transactions():  # 12
    cur.execute("""
                SELECT
                    customers.name || ' ' || customers.surname AS buyer,
                    SUM(sales.amount * sales.price) AS total_value                    
                FROM
                    sales
                INNER JOIN customers ON
                    sales.customer_id = customers.customer_id    
                GROUP BY buyer
                HAVING total_value = 
                                    (SELECT MAX(summ) 
                                    FROM
                                        (SELECT                                       
                                            SUM(amount * price) AS summ
                                        FROM
                                            sales                                       
                                        GROUP BY customer_id))
                """)
    rows = cur.fetchall()
    output = []
    output.append("{:<25}{:<10}".format(
        *[description[0] for description in cur.description]))
    for row in rows:
        output.append("{:<25}{:<10}".format(*row))
    print(*output, sep='\n')
    if input('Write to file? y/n ') == 'y':
        write_to_file(output)


def input_str(mask: str, invitation: str) -> str:
    while True:
        string = input('Enter ' + invitation + ' ')
        if re.fullmatch(mask, string):
            return string
        else:
            print('You made mistake, try one more')


def add_buyer(name=None, surname=None):
    if not name or not surname:
        name = input_str(r"[A-Z]\w+'?\w*", 'name')
        surname = input_str(r"[A-Z]\w+'?\w*", 'surname')
    cur.execute(f"""
                INSERT INTO customers 
                VALUES(NULL, '{name}', '{surname}')
                """)
    print('Buyer added')


def add_seller(name=None, surname=None):
    if not name or not surname:
        name = input_str(r"[A-Z]\w+'?\w*", 'name')
        surname = input_str(r"[A-Z]\w+'?\w*", 'surname')
    cur.execute(f"""
                INSERT INTO salesmen 
                VALUES(NULL, '{name}', '{surname}')
                """)
    print('Seller added')


def get_seller_id(seller_name):
    cur.execute(f"""
                SELECT seller_id
                FROM salesmen 
                WHERE name || ' ' || surname = '{seller_name}'
                """)
    rows = cur.fetchall()
    if rows:
        return rows.pop()[0]
    else:
        add_seller(*seller_name.split())
        return get_seller_id(seller_name)


def get_buyer_id(buyer_name):
    cur.execute(f"""
                SELECT customer_id
                FROM customers 
                WHERE name || ' ' || surname = '{buyer_name}'
                """)
    rows = cur.fetchall()
    if rows:
        return rows.pop()[0]
    else:
        add_buyer(*buyer_name.split())
        return get_buyer_id(buyer_name)


def add_deal():
    i = [
        # 'seller_id' INTEGER NOT NULL,
        get_seller_id(input_str(r"^[A-Z]\w+'?\w* [A-Z]\w+'?\w*$", 'seller')),
        # 'customer_id' INTEGER NOT NULL,
        get_buyer_id(input_str(r"^[A-Z]\w+'?\w* [A-Z]\w+'?\w*$", 'buyer')),
        input_str(r"^\d{2}[\./]\d{2}[\./]\d{4}$", 'date'),
        input_str(r".+", 'goods'),
        int(input_str(r"\d{1,7}", 'amount')),
        float(input_str(r"^\d{1,7}(?:\.\d\d)?$", 'price')),
    ]
    cur.execute("""
        INSERT INTO sales 
        VALUES(NULL, {},{},
        '{}','{}',{},{})
        """.format(*i))
    print('Deal added')


def select_for_insert():
    key = None
    while key != '0':
        print('Do you want to add a buyer(1), seller(2), or a deal(3)? (0) for exit to main menu')
        key = input('> ')
        if key == '1':
            add_buyer()
        elif key == '2':
            add_seller()
        elif key == '3':
            add_deal()
        elif key == '0':
            break
        else:
            print('You made a mistake')


def del_buyer():
    while True:
        enter = input('Enter buyer ID for delete ')
        if enter.isdecimal():
            buyer_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT customer_id
                FROM customers 
                WHERE customer_id = '{buyer_id}'
                """)
    rows = cur.fetchall()
    if rows:
        cur.execute(f"""
            DELETE FROM customers 
            WHERE customer_id = {buyer_id}
            """)
        print('Buyer deleted')
    else:
        print('No buyer with this ID')


def del_seller():
    while True:
        enter = input('Enter seller ID for delete ')
        if enter.isdecimal():
            seller_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT seller_id
                FROM salesmen 
                WHERE seller_id = '{seller_id}'
                """)
    rows = cur.fetchall()
    if rows:
        cur.execute(f"""
            DELETE FROM salesmen 
            WHERE seller_id = {seller_id}
            """)
        print('Seller deleted')
    else:
        print('No seller with this ID')


def del_deal():
    while True:
        enter = input('Enter deal ID for delete ')
        if enter.isdecimal():
            deal_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT invoice
                FROM sales 
                WHERE invoice = '{deal_id}'
                """)
    rows = cur.fetchall()
    if rows:
        cur.execute(f"""
            DELETE FROM sales 
            WHERE invoice = {deal_id}
            """)
        print('Deal deleted')
    else:
        print('No deal with this ID')


def select_for_delete():
    key = None
    while key != '0':
        print('Do you want to delete a buyer(1), seller(2), or a deal(3)? (0) for exit to main menu')
        key = input('> ')
        if key == '1':
            del_buyer()
        elif key == '2':
            del_seller()
        elif key == '3':
            del_deal()
        elif key == '0':
            break
        else:
            print('You made a mistake')


def update_buyer():
    while True:
        enter = input('Enter buyer ID for update ')
        if enter.isdecimal():
            buyer_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT customer_id
                FROM customers 
                WHERE customer_id = '{buyer_id}'
                """)
    rows = cur.fetchall()
    if rows:
        name = input_str(r"[A-Z]\w+'?\w*", 'name')
        surname = input_str(r"[A-Z]\w+'?\w*", 'surname')
        cur.execute(f"""
                    UPDATE customers
                    SET name = '{name}', 
                        surname = '{surname}'                    
                    WHERE customer_id = {buyer_id}
                    """)
        print('Buyer updated')
    else:
        print('No buyer with this ID')


def update_seller():
    while True:
        enter = input('Enter seller ID for update ')
        if enter.isdecimal():
            seller_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT seller_id
                FROM salesmen 
                WHERE seller_id = '{seller_id}'
                """)
    rows = cur.fetchall()
    if rows:
        name = input_str(r"[A-Z]\w+'?\w*", 'name')
        surname = input_str(r"[A-Z]\w+'?\w*", 'surname')
        cur.execute(f"""
                    UPDATE salesmen
                    SET name = '{name}', 
                        surname = '{surname}'                    
                    WHERE seller_id = {seller_id}
                    """)
        print('Seller updated')
    else:
        print('No seller with this ID')


def update_deal():
    while True:
        enter = input('Enter deal ID for update ')
        if enter.isdecimal():
            deal_id = int(enter)
            break
        else:
            print('You made a mistake')
    cur.execute(f"""
                SELECT invoice
                FROM sales 
                WHERE invoice = '{deal_id}'
                """)
    rows = cur.fetchall()
    if rows:
        i = [
            # 'seller_id' INTEGER NOT NULL,
            get_seller_id(
                input_str(r"^[A-Z]\w+'?\w* [A-Z]\w+'?\w*$", 'seller')),
            # 'customer_id' INTEGER NOT NULL,
            get_buyer_id(input_str(r"^[A-Z]\w+'?\w* [A-Z]\w+'?\w*$", 'buyer')),
            input_str(r"^\d{2}[\./]\d{2}[\./]\d{4}$", 'date'),
            input_str(r".+", 'goods'),
            int(input_str(r"\d{1,7}", 'amount')),
            float(input_str(r"^\d{1,7}(?:\.\d\d)?$", 'price')),
        ]
        cur.execute("""
            UPDATE sales 
            SET 'seller_id' = {},
                'customer_id' = {},
                'date' = '{}',
                'goods' = '{}',
                'amount' = {},
                'price' = {}             
            WHERE invoice = {}
            """.format(*i, deal_id))
        print('Deal updated')
    else:
        print('No deal with this ID')


def select_for_update():
    key = None
    while key != '0':
        print('Do you want to update a buyer(1), seller(2), or a deal(3)? (0) for exit to main menu')
        key = input('> ')
        if key == '1':
            update_buyer()
        elif key == '2':
            update_seller()
        elif key == '3':
            update_deal()
        elif key == '0':
            break
        else:
            print('You made a mistake')


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
                        ON DELETE CASCADE,
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
        select_for_insert()
    elif choice == '3':  # UPDATE
        select_for_update()
    elif choice == '4':  # DELETE
        select_for_delete()
    elif choice == 'exit':
        print('Goodbye!')
    else:
        print('You made a mistake')
con.commit()
cur.close()
