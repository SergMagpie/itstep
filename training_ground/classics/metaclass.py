class Metasecond(type):

    def __new__ (self, class_name, bases, attrs):
        attributes = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                attributes[key] = value
            else:
                attributes[class_name.lower() + '_' + key] = value

        return type(class_name, bases, attributes)

class Auto(metaclass=Metasecond):
    year = 2018
if __name__ == "__main__":
    
    a = Auto()
    print(dir(a))
