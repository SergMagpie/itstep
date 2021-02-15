num = int(input())
while num > 9:
    root = 0
    while num > 0:
        root += num % 10
        num //= 10
        # print(num, root)
        # input()
    num = root
print(num)
