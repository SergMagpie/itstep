def odd_numbers(num1, num2):
    if num1 % 2:
        return list(range(num1 + 1, num2, 2))
    else:
        return list(range(num1, num2, 2))

print(odd_numbers(3, 30))