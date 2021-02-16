class ExampleClass:
    __counter = 0
    varia = 1
    def __init__(self, val=1):
        self.__first = val
        ExampleClass.__counter += 1
        ExampleClass.varia = val


print('first print', ExampleClass.__dict__)
exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)
print(exampleObject1.__dict__,
      exampleObject1._ExampleClass__counter)
print(exampleObject2.__dict__,
      exampleObject2._ExampleClass__counter)
print(exampleObject3.__dict__,
      exampleObject3._ExampleClass__counter)

exampleObject = ExampleClass(2)
print(ExampleClass.__dict__)
print(exampleObject.__dict__)