def drow_line(long, gorizont, char):
    if gorizont:
        s = ''
    else:
        s = '\n'
    for _ in range(long):
        print(char, end=s)


drow_line(6, False, '8')
