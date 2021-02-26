from sortedcontainers import SortedDict
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
list_d = list(d.items()) 
list_d.sort(key=lambda i: i[1])
sorted_d_up = dict(list_d)
list_d.sort(key=lambda i: i[1], reverse=True)
sorted_d_down = dict(list_d)
print(sorted_d_up)
print(sorted_d_down)
# print(dict([(i, d[i]) for i in sorted(d, key=d.get, reverse=True)]))
result = dict([(i, d[i]) for i in sorted(d, key=d.get, reverse=False)])
print(result)
print(dict(SortedDict(d)))