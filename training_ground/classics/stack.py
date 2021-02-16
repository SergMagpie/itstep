class Stack:  # defining the Stack class
    def __init__(self):  # defining the constructor
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum


stackObject = AddingStack()
for i in range(5):
    stackObject.push(i)
print(stackObject.__dict__)
print(stackObject.getSum())
for i in range(5):
    print(stackObject.pop())
print(stackObject.__dict__)