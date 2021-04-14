from abc import ABCMeta, abstractclassmethod


class Warrior(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def walk():
        pass

    @abstractclassmethod
    def fire():
        pass

    @abstractclassmethod
    def say_name():
        pass


if __name__ == "__main__":
    class Child(Warrior):
        pass

    a = Child()
