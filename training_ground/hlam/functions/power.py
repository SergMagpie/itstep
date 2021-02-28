def power(n, p):
    if p == 1:
        return n
    else:
        return power(n, p - 1) * n

print(power(3, 3))