def same_pos(tup1: tuple, tup2: tuple, tup3: tuple) -> dict:
    rez = {}
    for num_poz, lis in enumerate(zip(tup1, tup2, tup3)):
        if lis[0] == lis[1] == lis[2]:
            rez[lis[0]] = num_poz
    return rez


print(same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1)))
