# We work for the result!
result = ''
# First, we check if these are number?
# There was no rejection of non-whole numbers
try:
    number = float(input())
# Secondly, we check if the numbers are in the range,
# and in order not to bother, we cause an error
    if not 1 <= number <= 100:
        1 / 0
# It could be written in three "if", but so cool
    if not number % 3:
        result += 'Fizz'
    if not number % 5:
        result += 'Buzz'
    print(result)
# Yes, yes, if not numbers then an exception
except:
    print('Dear user, you have entered invalid data!')
