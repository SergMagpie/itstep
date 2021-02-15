
baza = tuple(map(pow, range(1, 156), [5 for _ in range(155)]))


for a in baza:
    
    for b in baza:
        
        b1 = a + b
    
        for c in baza:
            c1 = b1 + c
        
            for d in baza:
                x = c1 + d
                if x > baza[-1]:
                    break
                if x in baza:
                    print('a =', baza.index(a)+1, 'b =', baza.index(b)+1,
                        'c =', baza.index(c)+1, 'd =',
                        baza.index(d)+1, 'e =', baza.index(x)+1, 'sum =',
                        baza.index(a)+1 + baza.index(b)+1 +
                        baza.index(c)+1 + baza.index(d)+1 + baza.index(x)+1)
                    exit()
