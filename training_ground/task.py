def sum_(n):
    i, rez = int(n), 0
    while i:
        rez += i % 10
        i //= 10
    return rez
def cont_(n):
    i, rez = int(n), 0
    while i:
        rez += 1
        i //= 10
    return rez
def total_(n):
    i, rez = int(n), 1
    while i:
        rez *= i % 10
        i //= 10
    return rez
def average_(n):
    return sum_(n) / cont_(n)
def first_(n):
    i = int(n)
    return i // 10 ** (cont_(n) - 1)
def sumfl_(n):
    return first_(n) + int(n) % 10
n = input()
print(sum_(n), cont_(n), total_(n), average_(n), first_(n), sumfl_(n), sep='\n')
