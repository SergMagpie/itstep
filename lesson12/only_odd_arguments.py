def only_odd_arguments(funk):
    def wrapper(*args):
        if all([i % 2 for i in args]):
            return funk(*args)
        else:
            print('Please add odd numbers')
    return wrapper


@only_odd_arguments
def add(a: int, b: int) -> int:
    return a + b


@only_odd_arguments
def multiply(a: int, b: int, c: int, d: int, e: int) -> int:
    return a * b * c * d * e


print(add(5, 5))
print(add(5, 6))
print(multiply(1, 2, 3, 4, 5))
print(multiply(1, 7, 3, 9, 5))
