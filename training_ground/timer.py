import time

start_time = time.time()
a = []
for i in range(9999999):
    a += [i]
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
b = [i for i in range(9999999)]
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
c = []
for i in a:
    if i % 2:
        c += [i ** 2]
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
d = [i ** 2 for i in b if i % 2]
print("--- %s seconds ---" % (time.time() - start_time))
