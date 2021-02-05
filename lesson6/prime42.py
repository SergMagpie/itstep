
prime42, next_num = [2, 3], 3
while len(prime42) < 42:
    next_num += 2
    for denominator in prime42:
        if next_num % denominator == 0:
            break
    else:
        prime42 += [next_num]
print(*prime42, sep=', ')
