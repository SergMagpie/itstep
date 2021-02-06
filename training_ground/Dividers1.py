a = int(input())
b = int(input())
max_number, max_sum_divaders = 0, 0
for number in range(b, a - 1, -1):
    sum_dividers = number
    for i in range(1, number // 2 + 1):
        if not number % i:
            sum_dividers += i
    if sum_dividers > max_sum_divaders:
        max_number, max_sum_divaders = number, sum_dividers
print(max_number, max_sum_divaders)
