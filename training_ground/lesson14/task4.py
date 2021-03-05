lis = (1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 6, 5)

set_lis = set(lis)
list_cont = []
for i in set_lis:
    counter = 0
    for j in lis:
        if i == j:
            counter += 1
    list_cont.append(counter)
count_i = []
for i in set(list_cont):
    con = 0
    for j in list_cont:
        if i == j:
            con += 1
    count_i.append(con)

print(*[f'Numbers {i + 1} in tuple {j}' for i,
        j in enumerate(count_i)], sep='\n')
