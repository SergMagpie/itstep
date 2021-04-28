from multiprocessing import Process, Lock
 
 
def printer(item, lock):
    """
    Выводим то что передали
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()
 
 
if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()