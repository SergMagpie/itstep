import os
from time import time
from multiprocessing import Process
from threading import Thread

global_count = 0
def calculate_in_process(num):
    global global_count
    result = num * 4
    print(f"Result -> {result} | Global counter -> {global_count} in process ID ", os.getpid())
    global_count += result


if __name__ == "__main__":

    lst_for_calculate = [2, 4, 20, 50, 120, 9, ]
    process_list = []
    x1 = time()
    for n in lst_for_calculate:
        p = Thread(target=calculate_in_process, args=(n,))
        # p = Process(target=calculate_in_process, args=(n,))
        process_list.append(p)
        p.start()
    
    for p in process_list:
        p.join()
    x2 = time()
    print(x2-x1)

