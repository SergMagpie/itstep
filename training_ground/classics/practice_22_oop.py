class CloneTrooper():
    __counter = 0
    def __init__(self):
        self.__id = CloneTrooper.__counter
        CloneTrooper.__counter += 1

    def fight(self):
        print("I am CloneTrooper", self.__id, 'started fight')


    def say_name(self):
        print("I am CloneTrooper", self.__id)

if __name__ == "__main__":
    stek = []
    for i in range(10):
        stek.append(CloneTrooper())
    [i.fight() for i in stek]
    [i.say_name() for i in stek]
