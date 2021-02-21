s = "Hawnj pk swhg xabkna ukq nqj."
const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' # Строчные буквы
for j in range(-25,26):
    s1 = []
    for i in s:
        if i in const_upper_en:
            s1 += const_upper_en[const_upper_en.index(i) - j]
        elif i in const_lower_en:
            s1 += const_lower_en[const_lower_en.index(i) - j]
        else:
            s1 += i
    print(''.join(s1))
