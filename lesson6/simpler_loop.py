print(*range(0, 146, 5))
# maybe I misunderstood the task
# and it was necessary to write something like
number = 0
for cont in range(30):
    print(number, end=' ')
    number += 1
    while number % 5:
        number += 1
# I checked it also works
# but the first option I like more
