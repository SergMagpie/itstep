rows = 15
cont = 1
for _ in range(rows):
    string = '*' * cont
    print(string.center(rows * 2 + 1))
    cont += 2
