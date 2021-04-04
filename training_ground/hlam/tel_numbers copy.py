def convert_to_number(word: str) -> str:
    num_lit = {'i': 1, 'j': 1, 'a': 2, 'b': 2, 'c': 2,
               'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4,
               'k': 5, 'l': 5, 'm': 6, 'n': 6, 'p': 7,
               'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8,
               'w': 9, 'x': 9, 'y': 9, 'o': 0, 'q': 0,
               'z': 0}
    return ''.join([str(num_lit[letter]) for letter in word])

from sys import stdin
in_dates=stdin.read().split()
number_of_string = 0

phone_num = in_dates[number_of_string]
len_phone_num = len(phone_num)
word_count = int(in_dates[number_of_string + 1])
words = in_dates[number_of_string + 2: number_of_string + word_count + 2]
number_of_string += word_count + 2

array = [[-1] * (len_phone_num + 1) for i in range(len_phone_num + 1)]
word_numbers = [convert_to_number(words[i]) for i in range(word_count)]

for i in range(len_phone_num):
    for k in range(word_count):
        number = word_numbers[k]
        number_length = len(number)
        if phone_num[i: i + number_length] == number:
            array[i][i + number_length] = k


vertex = [(10000000, -1, -1)] * (len_phone_num + 1)
stack = []
stack.append(0)
vertex[0] = (0, 0, 0)
while stack:
    top = stack.pop()
    ver = vertex[top]
    new_weight = ver[0] + 1
    for j in range(top + 1, len_phone_num + 1):
        k = array[top][j]
        if k > -1:
            v = vertex[j]
            if v[0] > new_weight:
                if v[1] == -1:
                    stack.append(j)
                vertex[j] = (new_weight, top, k)

rver = vertex[len_phone_num]
if rver[1] == -1:
    print('No solution.')
else:
    way = []
    pos = len_phone_num
    while pos != 0:
        v = vertex[pos]
        way.insert(0, words[v[2]])
        pos = v[1]
    print(' '.join(way))


