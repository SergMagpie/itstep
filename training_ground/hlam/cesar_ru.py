s = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
s1 = []
for i in s:
    if i in const_upper_ru:
        s1 += const_upper_ru[const_upper_ru.index(i) - 7]
    elif i in const_lower_ru:
        s1 += const_lower_ru[const_lower_ru.index(i) - 7]
    else:
        s1 += i
print(''.join(s1))
