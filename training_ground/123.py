for a in range(33):
    for b in range(33):
        for c in range(33):
            for d in range(33):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and b != c and c != d and a != c and a != d:
                    print(a, b, c, d, a**3+b**3)
