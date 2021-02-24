# task 1 -------------------------------------------------
print('task 1 ----------------------------------------------\n')


def gen_any_3():
    for i in range(3, 230, 3):
        yield i


gen = gen_any_3()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen2 = iter(range(3, 230, 3))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

# task 2--------------------------------------------------------------
print('\ntask 2 -----------------------------------------------\n')


def do_twice(funk_to_decorate):
    def wrapper():
        print('Funk for decor is decorated and it is runing twice')
        funk_to_decorate()
        funk_to_decorate()
    return wrapper


@do_twice
def funk_for_dekor():
    print("I'm funk for dekor")


funk_for_dekor()

# task 3--------------------------------------------
print('\ntask 3 -----------------------------\n')


def repeat(funk):
    def wrapper(times=1):
        for _ in range(times):
            funk(times)
    return wrapper


@repeat
def funk_for_repeat(n):
    print(f'Funk for repeat {n} times')


funk_for_repeat(4)
