class Army:
    pass


class OrcArmy:
    def __init__(self, warior_amount, damage_per_orc, warrior_health) -> None:
        self.warior_amount = warior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health

    def __add__(self, other):
        """Implements addition."""
        new_amount = self.warior_amount + other.warior_amount
        new_damage = int((self.damage_per_orc * self.warior_amount +
                          other.damage_per_orc * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_health = int((self.warrior_health * self.warior_amount +
                          other.warrior_health * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        return OrcArmy(new_amount, new_damage, new_health)

    def __sub__(self, other):
        """Implements subtraction."""
        new_amount = self.warior_amount - other.warior_amount
        if new_amount < 0:
            new_amount = 0
        new_damage = int((self.damage_per_orc * self.warior_amount +
                          other.damage_per_orc * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_health = int((self.warrior_health * self.warior_amount +
                          other.warrior_health * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        return OrcArmy(new_amount, new_damage, new_health)

    def __str__(self) -> str:
        if self.warior_amount > 0:
            warior_amount = self.warior_amount
        else:
            warior_amount = 'Army is destroyed'
        return ' '.join([str(i) for i in
                         ['Orc ', warior_amount, self.damage_per_orc,
                          self.warrior_health]])

    def receive_damage(self, damage: int):
        self.warior_amount = self.warior_amount - damage // self.warrior_health


class ElfArmy:
    def __init__(self, warior_amount, damage_per_orc, warrior_health, shield) -> None:
        self.warior_amount = warior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health
        self.shield = shield

    def __add__(self, other):
        """Implements addition."""
        new_amount = self.warior_amount + other.warior_amount
        new_damage = int((self.damage_per_orc * self.warior_amount +
                          other.damage_per_orc * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_health = int((self.warrior_health * self.warior_amount +
                          other.warrior_health * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_shield = int((self.shield * self.warior_amount +
                          other.shield * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        return ElfArmy(new_amount, new_damage, new_health, new_shield)

    def __sub__(self, other):
        """Implements subtraction."""
        new_amount = self.warior_amount - other.warior_amount
        if new_amount < 0:
            new_amount = 0
        new_damage = int((self.damage_per_orc * self.warior_amount +
                          other.damage_per_orc * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_health = int((self.warrior_health * self.warior_amount +
                          other.warrior_health * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        new_shield = int((self.shield * self.warior_amount +
                          other.shield * other.warior_amount) /
                         (self.warior_amount + other.warior_amount))
        return ElfArmy(new_amount, new_damage, new_health, new_shield)

    def __str__(self) -> str:
        if self.warior_amount > 0:
            warior_amount = self.warior_amount
        else:
            warior_amount = 'Army is destroyed'
        return ' '.join([str(i) for i in
                         ['Elf ', warior_amount, self.damage_per_orc,
                          self.warrior_health, self.shield]])

    def receive_damage(self, damage: int):
        self.warior_amount = self.warior_amount - \
            damage // (self.warrior_health + self.shield)


if __name__ == "__main__":
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
