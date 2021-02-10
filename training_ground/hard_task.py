a = [1, 3, 6, 9]
b = [2, 3, 4, 5, 6, 7]
# third list containing elements of both lists
c = a + b
# third list containing elements of both lists without repetitions
d = list(set(a + b))
# a third list containing elements common to the two lists
e = [i for i in a if i in b]
# a third list containing only the unique elements of each of the lists
f = [i for i in a + b if i not in [i for i in a if i in b]]
# a third list containing only the minimum and maximum value of each of the lists
g = [min(a), max(a), min(b), max(b)]
# for index, elem in enumerate(g):
#     print(index, elem)
print(c)
print(d)
print(e)
print(f)
