class CloneTrooper():

    def __init__(self, id):
        self.__id = id

    def fight(self):
        print("I am CloneTrooper", self.__id, 'started fight')

    def say_name(self):
        print("I am CloneTrooper", self.__id)


class StormTrooper(CloneTrooper):
    def __init__(self, id):
        super().__init__(id)
        self.__id = "ST-" + id

    def type(self):
        print('Trooper type -> StormTrooper', self.__id)


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
