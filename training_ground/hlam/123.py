import random
KeyList = ['1:00', '2:00', '3:00', '4:00', '5:00',
           '6:00', '7:00', '8:00', '9:00', '10:00',
           '11:00', '12:00', '13:00', '14:00', '15:00',
           '16:00', '17:00', '18:00', '19:00', '20:00',
           '21:00', '22:00', '23:00', '24:00']
# словарь для записи в значение играл/не играл(0 - не играл, 1 - играл)
time = {}
for i in KeyList:
    time[i] = random.randint(0, 1)

print(time)

# перенос значений в список, чтобы сравнить два списка
values = []
for v in time.values():
    values.append(v)
print(KeyList)
print(values)

# собственно, решение задачи
count = 0
max_item = 0
for i in time.values():
    if i:
        count += 1
    else:
        count = 0
    if count > max_item:
        max_item = count
print(max_item)
