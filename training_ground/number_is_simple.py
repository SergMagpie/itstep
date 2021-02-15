def is_num_simple(number):

    if number == 2 or number == 3:
        return True
    elif number > 4:
        for test in range(2, int(number ** 0.5 + 1)):
            if number % test == 0:
                return False
            else:
                return True
    else:
        return False


for i in range(20):
    print('number {} is simple - {}'.format(i, is_num_simple(i)))
