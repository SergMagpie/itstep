class Super:
    def __init__(self, name):
        self.name = name
        self.a = 1
        self.b = 2

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)
        self.a = 3
        self.b = 4


obj = Sub("Andy")
print(obj, obj.a, obj.b)
