
import fib

import time

start_time = time.time()
print(*[fib.fib(i) for i in range(30)])
print("-time recursion-- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(*fib.fib_num(30))
print("-time iteration-- %s seconds ---" % (time.time() - start_time))