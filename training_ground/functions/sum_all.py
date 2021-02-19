def sum_all(a, b):
    if a == b:
        return b
    else:
        return sum_all(a + 1, b) + a

print(sum_all(1, 4))