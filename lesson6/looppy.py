# interesting puzzle
for i in range(100, 0, -1):
    number = str(i)
    if number[0] == number[-1]:
        print(number, end=' ')
print()
