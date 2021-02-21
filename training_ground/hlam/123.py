def f(a=[0]):
    a[0] += 1
    return a[0]

print(*[f() for _ in range(10)])