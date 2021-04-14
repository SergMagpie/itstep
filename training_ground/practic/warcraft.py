from abstract import Warrior


class Sword:
    def attack(self):
        print('Sword attack!')


class Bow:
    def attack(self):
        print('Bow attack!')


class Orc(Warrior):
    def __init__(self, weapon) -> None:
        super().__init__()
        self.weapon = weapon

    def walk(self):
        pass

    def fire(self):
        self.weapon.attack()

    def say_name(self):
        pass


if __name__ == "__main__":
    a = Sword()
    b = Bow()
    fregl = Orc(a)
    frody = Orc(b)
    fregl.fire()
    frody.fire()
