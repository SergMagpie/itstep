def unique(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    return tuple((set(tup1) | set(tup2) | set(tup3)) -
                 ((set(tup1) & set(tup2)) |
                  (set(tup1) & set(tup3)) |
                  (set(tup2) & set(tup3))))


print(unique((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))
