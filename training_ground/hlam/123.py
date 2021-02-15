first_num = []
for i in range(2, 300):
    for g in range(2, i):
        if i % g == 0:
            break
    else:
        first_num.append(i)
    if len(first_num) == 35:
        break
print(*first_num, sep=", ")

