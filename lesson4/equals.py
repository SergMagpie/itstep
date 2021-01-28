# First we check to see if they are numbers?
try:
    number1, number2 = float(input()), float(input())
# Cut off zeroes if numbers are integers
    if not number1 % 1:
        number1 = int(number1)
    if not number2 % 1:
        number2 = int(number2)
# Checking the equality of numbers
    if number1 == number2:
        print('EQUALS')
# If the numbers are not equal, some number must be greater
    elif number1 < number2:
        print(number2, number1)
# No other is given
    else:
        print(number1, number2)
# Yes, yes, if not numbers then an exception
except:
    print('Am I a Joke to You?')
