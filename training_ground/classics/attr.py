class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
        self.__c = 3
        self._d = 4


exampleObject = ExampleClass()
print(hasattr(exampleObject, 'b'))
print(hasattr(exampleObject, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
print(ExampleClass.__dict__)
print(exampleObject.__dict__)
print(exampleObject._ExampleClass__c)