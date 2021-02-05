rows = input('Please enter the number of rows of the pyramid or 0 for exit: ')
while rows != '0':
    if rows.isdigit():
        rows = int(rows)
        cont = 1
        for _ in range(rows):
            string = '*' * cont
            print(string.center(rows * 2 + 1))
            cont += 2
    else:
        print('You were wrong')
    rows = input(
        'Please enter the number of rows of the pyramid or 0 for exit: ')
