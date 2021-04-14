class CustomMeta(type):

    def __new__(cls, class_name, bases, attrs):
        attributes = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                attributes[key] = value
            else:
                attributes['method_' + key] = value
        attributes['class_name'] = class_name.lower()
        return super(CustomMeta, cls).__new__(cls, class_name, bases, attributes)


if __name__ == "__main__":
    class Proba(metaclass=CustomMeta):

        def __init__(self):
            self.atr = 'ATR'

        def method1(self):
            print('Method1')

        def method2(self):
            print('Method2')

    a = Proba()
    print(a.__dict__)
    print(dir(a))
    print(a.class_name)
    a.method_method1()
    a.method_method2()
    print(a.__dict__)
