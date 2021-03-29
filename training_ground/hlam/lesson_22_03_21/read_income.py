import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



income = {}
with open("example", 'r') as f:
    for line in f:
        data = line.split()
        income[data[0]] = data[1]
print(income)