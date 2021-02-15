##baza = list(map(pow, range(1,156), [5 for _ in range(155)]))
##a = 14348907
##b = 4182119424
##c = 16105100000
##d = 41615795893
##e = 61917364224
##print(baza.index(a)+1 + baza.index(b)+1 +
##baza.index(c)+1 + baza.index(d)+1 + baza.index(e)+1)

from datetime import datetime
start_time = datetime.now()

##arr5 = [i ** 5 for i in range(2, 150)]                           # массив пятых степеней
##abc = set(a + b + c for a in arr5 for b in arr5 for c in arr5)   # варианты сумм а^5+b^5+ c^5
##de =  set(e - d  for e in arr5 for d in arr5 if e - d > 0)       # варианты разности е^5 - d^5
##res = abc & de                                                   # пересечение вариантов
##
### находим a b c для верных ответов
##abc_res = [[a + b + c, a, b, c] for a in arr5 for b in arr5 for c in arr5 if a + b + c in res]  
##
### находим d e для верных ответов 
##de_res = [[e - d, e , d]  for e in arr5 for d in arr5 if (e - d in res) ]
##
##elist = []
##for i_res in res:            #  исключаем повторения
##    for i_abc in abc_res:                
##        if i_res == i_abc[0]:
##            aa, bb, cc = i_abc[1:]   
##    for i_de in de_res:
##        if i_res == i_de[0]:
##            ee, dd = i_de[1:]
##    if ee not in elist:     
##        elist.append(ee)
##        aa, bb, cc, dd, ee = sorted([round(aa**0.2), round(bb**0.2), round(cc**0.2), round(dd**0.2), round(ee**0.2)])
##        print(aa, bb, cc, dd, ee,'a+b+c+d+e=',aa + bb + cc + dd + ee)


for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
