from math import ceil, sqrt


def mindivisor(number):
    # manually test 1, 2, 3 and multiples of 2 and 3
    if number == 1:
        return 1
    elif number % 2 == 0:
        return 2
    elif number % 3 == 0:
        return 3

    # we can now avoid to consider multiples
    # of 2 and 3. This can be done really simply
    # by starting at 5 and incrementing by 2 and 4
    # alternatively, that is:
    #    5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, ...
    # we don't need to go higher than the square root of the number
    divisor = 5
    increment = 2
    sqrt_n = ceil(sqrt(number))
    while divisor <= sqrt_n:
        if number % divisor == 0:
            return divisor
        divisor += increment
        increment = 6 - increment  # 2 -> 4 -> 2

    return number  # number is prime
numeric = int(input())
print(mindivisor(numeric))