from functools import reduce

old_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

new_list = reduce(lambda x, y: x * y, old_list)

print(new_list)
