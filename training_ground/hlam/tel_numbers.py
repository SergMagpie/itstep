def dig_dic(vocab):
    num_lit={'i':1,'j':1,'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,
             'k':5,'l':5,'m':6,'n':6,'p':7,'r':7,'s':7,'t':8,'u':8,'v':8,
             'w':9,'x':9,'y':9,'o':0,'q':0,'z':0}
    dic={}
    for word in vocab:        
        dic[''.join([str(num_lit[letter]) for letter in word])] = word
    return dic

def finder(number,dic,way=[]):
    ways=[];    way_ = ''.join(way)
    list_dic=[i for i in [k for k in dic if k in number[len(way_):]]
              if number[len(way_):].find(i) == 0]
    for i in list_dic:
        if i == number[len(way_):]:
            return True, way+[i]
    for i in list_dic:
        flag, way_rez = finder(number,dic,way+[i])
        if flag:
            ways.append(way_rez)
    if ways:
        return True, sorted(ways,key=len)[0]
    return False, []

import time
start_time = time.time()

from sys import stdin
#in_dates=stdin.read().split()
def load_dates():
    in_dates=open('dates.txt', 'r').read().split(sep='\n')
    list_tasks=[]; i=0
    while in_dates[i] != '-1':
        num = in_dates[i];
        cont_words = int(in_dates[i+1]);
        vocab = in_dates[i+2:i+cont_words+2];
        i += cont_words + 2;
        list_tasks.append([num,vocab])
    return list_tasks

for number, vocab in load_dates():
    flag, result=finder(number,dig_dic(vocab).keys())
    if flag == False:
        m=['No solution.']
    else:
        m=list(map(lambda i:dig_dic(vocab)[i],result))
    print(*m)
print("--- %s seconds ---" % (time.time() - start_time))
