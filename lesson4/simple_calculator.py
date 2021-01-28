# Cut off zeroes if numbers are integers (Beautiful is better than ugly)
def cut_off_zeroes(float_number):
    if not float_number % 1:
        return int(float_number)
    else:
        return float_number


# First, we check if these are numbers?
try:
    number1 = cut_off_zeroes(float(input()))
    symbol_of_mathematical_action = input()
# Secondly, we check if the symbol of mathematical action is as follows
    if not symbol_of_mathematical_action in ('+', '-', '*', '/'):
        1/0
    number2 = cut_off_zeroes(float(input()))
# We print the results of operations
    if symbol_of_mathematical_action == '+':
        print(number1, symbol_of_mathematical_action, number2, '=',
              cut_off_zeroes(number1 + number2))
    elif symbol_of_mathematical_action == '-':
        print(number1, symbol_of_mathematical_action, number2, '=',
              cut_off_zeroes(number1 - number2))
    elif symbol_of_mathematical_action == '*':
        print(number1, symbol_of_mathematical_action, number2, '=',
              cut_off_zeroes(number1 * number2))
    elif symbol_of_mathematical_action == '/':
        print(number1, symbol_of_mathematical_action, number2, '=',
              cut_off_zeroes(number1 / number2))
# Yes, yes, if not numbers, not arithmetic signs or division zero
# then an exception
except:
    print('Dear user, you have entered invalid data!')
