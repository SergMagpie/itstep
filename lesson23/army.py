class Army:
    def __init__(self,
                 warior_amount,
                 damage_per_orc,
                 warrior_health,
                 shield=0) -> None:
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
        return self.__class__(new_amount, new_damage, new_health, new_shield)

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
        return self.__class__(new_amount, new_damage, new_health, new_shield)

    def __str__(self) -> str:
        if self.warior_amount > 0:
            warior_amount = self.warior_amount
        else:
            warior_amount = 'Army is destroyed'
        return ' '.join([str(i) for i in
                         [self.__class__.__name__, warior_amount, self.damage_per_orc,
                          self.warrior_health, self.shield]])

    def receive_damage(self, damage: int):
        self.warior_amount = self.warior_amount - \
            damage // (self.warrior_health + self.shield)


class OrcArmy(Army):
    def __init__(self,
                 warior_amount,
                 damage_per_orc,
                 warrior_health,
                 shield=0) -> None:
        super().__init__(
                       warior_amount,
                       damage_per_orc,
                       warrior_health,
                       shield)


class ElfArmy(Army):
    def __init__(self,
                 warior_amount,
                 damage_per_orc,
                 warrior_health,
                 shield) -> None:
        super().__init__(
                       warior_amount,
                       damage_per_orc,
                       warrior_health,
                       shield)
