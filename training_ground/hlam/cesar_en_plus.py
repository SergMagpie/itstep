s = 'Day, mice. "Year" is a mistake!'
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' # Строчные буквы
for elem in s.split():
    j = len([i for i in elem if i.isalpha()])
    s1 = []
    for i in elem:
        if i in const_upper_en:
            s1 += const_upper_en[const_upper_en.index(i) + j]
        elif i in const_lower_en:
            s1 += const_lower_en[const_lower_en.index(i) + j]
        else:
            s1 += i
    print(''.join(s1), end=' ')
