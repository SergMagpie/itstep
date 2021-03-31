class CloneTrooper():

    def __init__(self, id):
        self._identificator = id
        self.name = 'CT-' + id

    def fight(self):
        print("I am CloneTrooper", self.name, 'started fight')

    def say_name(self):
        print("I am CloneTrooper", self.name)

    def __eq__(self, other):
        '''
        Определяет поведение оператора равенства, ==.
        '''
        if self._identificator == other._identificator:
            return True
        else:
            return False

    def __ne__(self, other):
        '''
        Определяет поведение оператора неравенства, !=.
        '''
        if self._identificator != other._identificator:
            return True
        else:
            return False

    def __lt__(self, other):
        '''
        Определяет поведение оператора меньше, < .
        '''
        if self._identificator < other._identificator:
            return True
        else:
            return False

    def __gt__(self, other):
        '''
        Определяет поведение оператора больше, > .
        '''
        if self._identificator > other._identificator:
            return True
        else:
            return False

    def __le__(self, other):
        '''
        Определяет поведение оператора меньше или равно, <= .
        '''
        if self._identificator <= other._identificator:
            return True
        else:
            return False

    def __ge__(self, other):
        '''
        Определяет поведение оператора больше или равно, >= .:
        '''
        if self._identificator >= other._identificator:
            return True
        else:
            return False

    def __str__(self):
        return "I'm " + self.name


class StormTrooper(CloneTrooper):
    def __init__(self, id):
        super().__init__(id)
        self.name = 'ST-' + id

    def fight(self):
        print("I am CloneTrooper", "ST-" + self._identificator, 'started fight')

    def say_name(self):
        print("I am CloneTrooper", "ST-" + self._identificator)

    @staticmethod
    def type():
        print('Trooper type -> StormTrooper')


if __name__ == "__main__":
    stek = []
    stek2 = []
    for i in range(10):
        stek.append(CloneTrooper(str(i)))
    [i.fight() for i in stek]
    [i.say_name() for i in stek]
    for i in range(10):
        stek2.append(StormTrooper(str(i)))
    [i.fight() for i in stek2]
    [i.say_name() for i in stek2]
    [i.type() for i in stek2]
    for i in stek:
        for j in stek2:
            print(i, '==', j, i == j)
