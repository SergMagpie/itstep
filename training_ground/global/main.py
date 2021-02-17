import coocoo, fib
global pi
pi = 3.14

def main():
    print(coocoo.coocoo(pi))

main()

print(*[fib.fib(i) for i in range(1, 10)])