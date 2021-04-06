from characters import *

a1 = OrcArmy(100, 50, 80)
a2 = OrcArmy(200, 100, 160)
a3 = a1 + a2
print(a1)
print(a2)
print(a3)
a4 = a3 - a1
print(a4)
a4.receive_damage(300)
print(a4)
b1 = ElfArmy(100, 50, 80, 30)
b2 = ElfArmy(200, 100, 160, 30)
b3 = b1 + b2
print(b1)
print(b2)
print(b3)
b4 = b3 - b1
print(b4)
b4.receive_damage(500)
print(b4)
steck = [a1, a2, a3, a4, b1, b2, b3, b4]
damage = 0
while damage != 'exit':
    damage = input('Enter damage or exit for exit ')
    if damage.isdigit():
        damage = int(damage)
        for i in steck:
            i.receive_damage(damage)
        print(*steck, sep="\n")
    elif damage == 'exit':
        print('Good by!')
    else:
        print('You made a mistake')
