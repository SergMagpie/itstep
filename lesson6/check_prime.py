number = input('Input number or 0 for exit: ')
while number != '0':
    if number.isdigit():
        numb_for_test = int(number)
        flag = False
        if numb_for_test == 2 or numb_for_test == 3:
            flag = True
        elif numb_for_test > 4:
            for test in range(2, int(numb_for_test ** 0.5 + 1)):
                if numb_for_test % test == 0:
                    break
            else:
                flag = True
        print(f'The number is', ['complex', 'prime'][flag])
    else:
        print('You were wrong')
    number = input('Input number or 0 for exit: ')
