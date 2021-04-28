from time import time
from threading import Thread
import os
# Actualised a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def input_path_to_file(num):
    while True:
        path = input(f"Enter name of {num} file: ")
        try:
            with open(path, "r") as f:
                data = f.readline()
            return path
        except FileNotFoundError:
            print('You made a mistake')


def find_word_in_file(path, word):
    with open(path, "r") as f:

        for n, line in enumerate(f):
            if word in line:
                print(f"Word is in {n} string of file {path}")


if __name__ == "__main__":

    path = input_path_to_file('first')
    path2 = input_path_to_file('second')
    word = input('Enter word for find ')
    time1 = time()
    t1 = Thread(target=find_word_in_file, args=(path, word))
    t2 = Thread(target=find_word_in_file, args=(path2, word))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time2 = time()
    print(time1 - time2)
