a, b = int(input()), int(input())
if a == 1:
    a = 2
for i in range(a, b + 1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        print(i)
