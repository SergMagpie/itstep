from sys import stdin
def dig_dic(vocab):
    num_lit = {'i': 1, 'j': 1, 'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4,
               'k': 5, 'l': 5, 'm': 6, 'n': 6, 'p': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8,
               'w': 9, 'x': 9, 'y': 9, 'o': 0, 'q': 0, 'z': 0}
    dic = {}
    for word in vocab:
        dic[''.join([str(num_lit[letter]) for letter in word])] = word
    return dic


def finder(number: str, dic: dict):
    def list_dic(number: str, way):
        way_ = ''.join(way)
        return [[i] for i in [k for k in dic if k in number[len(way_):]]
                if number[len(way_):].find(i) == 0]

    ways = list_dic(number, [])
    while ways:
        for i in ways:
            if ''.join(i) == number:
                return ' '.join(map(lambda x: dic[x], i))
            i1 = list_dic(number, i)
            if i1:
                ways.append(i + i1[0])
            else:
                ways.remove(i)
    return 'No solution.'

in_dates = stdin.read().split()
num = in_dates[0]
vocab = in_dates[2:int(in_dates[1])+2]
print(finder(num, dig_dic(vocab)))
