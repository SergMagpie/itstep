from sys import stdin
def dig_dic(vocab):
    num_lit = {'i': 1, 'j': 1, 'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4,
               'k': 5, 'l': 5, 'm': 6, 'n': 6, 'p': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8,
               'w': 9, 'x': 9, 'y': 9, 'o': 0, 'q': 0, 'z': 0}
    dic = {}
    for word in vocab:
        dic[''.join([str(num_lit[letter]) for letter in word])] = word
    return dic


def finder_long(number,dic,way=[]):
    ways=[];    way_ = ''.join(way)
    list_dic=[i for i in [k for k in dic if k in number[len(way_):]]
              if number[len(way_):].find(i) == 0]
    for i in list_dic:
        if i == number[len(way_):]:
            return True, way+[i]
    for i in list_dic:
        flag, way_rez = finder_long(number,dic,way+[i])
        if flag:
            ways.append(way_rez)
    if ways:
        return True, sorted(ways,key=len)[0]
    return False, []



in_dates = stdin.read().split()
num = in_dates[0]
vocab = in_dates[2:int(in_dates[1])+2]
dic = dig_dic(vocab)
flag, result = finder_long(num, dic) 
if flag == False:
    m = ['No solution.']
else:
    m = list(map(lambda i: dic[i], result))
print(*m)
