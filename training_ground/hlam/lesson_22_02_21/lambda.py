def custom_mul(n):
    return lambda a: a * n

doubler = custom_mul(2)
print(doubler(5))

triple = custom_mul(43)
print(triple(5))