import time
start_time = time.time()
a=100

##for i in range(1, a + 1):
##  for j in range(1, 10):
##    print(f'{i} + {j} = {i + j}')
##  print()
[[print(f'{j} + {i} = {j+i}') for i in range(1,10)]and print() for j in range(1,a+1)]
print("--- %s seconds ---" % (time.time() - start_time))
