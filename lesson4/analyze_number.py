# First, we check if these are integer number?
try:
    number = int(input())
# Secondly, we check if the number is parity
    if number % 2:
        parity_indication = 'odd'
    else:
        # Zero is even number
        parity_indication = 'even'
# Thirdly, we check the sign of positivity
    if number > 0:
        positivity_indication = 'positive'
    elif number < 0:
        positivity_indication = 'negative'
    else:
        positivity_indication = 'zero'
    print(number, positivity_indication, parity_indication, 'number')
# Yes, yes, if not numbers then an exception
except:
    print('Dear user, you have entered invalid data!')
