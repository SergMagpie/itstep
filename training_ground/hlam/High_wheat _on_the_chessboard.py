b, c = 1, 0
for i in range(1,65):
    c += b
    print(i, b, c)
    b *= 2
m = c * 0.065 / 1000 / 1000
print('mass tonn', m)
maxvol = m * 3.33
minvol = m * 1.22
print('volume m2', maxvol, minvol)
highmax = maxvol / 149000000
highmin = minvol / 149000000
print('high m', highmax, highmin)
