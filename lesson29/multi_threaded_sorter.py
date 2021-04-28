# multi-threaded sorter MTS-1 by SergMagpie
from time import time
from threading import Thread
import os
import random
import json
# Actualised a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def create_file_of_numbers(quantity=10000, filename='random_numbers.json'):
    start_time = time()
    with open(filename, "a") as f:
        dates = []
        for _ in range(quantity):
            dates.append(random.randint(-99, 99))
        json.dump(dates, f, indent=4)
    finish_time = time()
    spent_time = finish_time - start_time
    print(f"a new file '{filename}' of {quantity} numbers has been created")
    print(f"spent time {spent_time}")


print("All the best to you!")
print("Welcome to the multi-threaded sorter MTS-1!")
print("If you have a file with numbers,")
print("enter the name of this file or enter nothing")
while True:
    path = input("Enter the name of a file with numbers: ")
    if path:
        try:
            with open(path, "r") as f:
                data = f.readline()
            break
        except FileNotFoundError:
            print('You made a mistake')
    else:
        create_file_of_numbers()
        break

