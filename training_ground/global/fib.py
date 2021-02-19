def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_num(n):
    fib1 = fib2 = 1
    f = []
    if n < 2:
        quit()

    f += [fib1]
    f += [fib2]
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        f += [fib2]
    return f
