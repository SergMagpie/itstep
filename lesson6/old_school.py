mult = input('Input number or 0 for exit: ')
while mult != '0':
    if mult.isdigit():
        mult1 = int(mult)
        for mult2 in range(1, 11):
            print(f'{mult1} * {mult2} = {mult1 * mult2}')
    else:
        print('You were wrong')
    mult = input('Input number or 0 for exit: ')
