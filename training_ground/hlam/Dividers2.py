a = int(input())
for number in range(1, a + 1):
    cont_dividers = 1
    for i in range(1, number // 2 + 1):
        if not number % i:
            cont_dividers += 1
    print(number, '+' * cont_dividers)
