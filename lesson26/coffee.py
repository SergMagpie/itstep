from abc import ABCMeta, abstractclassmethod


class Coffee(metaclass=ABCMeta):
    names_of_coffee = {'Arabica',
                       'Robusta',
                       'Liberica',
                       'Excelsa',
                       'Typica',
                       'Kona',
                       'Java',
                       'Jamaican Blue Mountain',
                       'Sumatra',
                       'Bergendal',
                       'Rume Sudan',
                       'Amarello de Botancatú',
                       'Blawan Paumah',
                       'Java Mocha',
                       'Pluma Hidalgo',
                       'Creole',
                       'Ethiopian Harrar',
                       'Blue Mountain',
                       'Villa Sarchi',
                       'Ethiopian Sidamo',
                       'Ethiopian Yiragacheffe',
                       'San Ramón',
                       'Sidikalang'
                       }

    def __init__(self,
                 size,
                 name,
                 milk,
                 to_go
                 ) -> None:
        self.size = size
        self.name = name
        self.milk = milk
        self.to_go = to_go

    @abstractclassmethod
    def get_cup_size():
        '''returns the size of a cup of coffee'''
        pass

    @abstractclassmethod
    def coffee_name():
        '''
        Arabica 
        Robusta
        Liberica
        Excelsa
        Typica 
        Kona
        Java
        Jamaican Blue Mountain
        Sumatra
        Bergendal
        Rume Sudan
        Amarello de Botancatú
        Blawan Paumah
        Java Mocha
        Pluma Hidalgo
        Creole
        Ethiopian Harrar
        Blue Mountain
        Villa Sarchi
        Ethiopian Sidamo
        Ethiopian Yiragacheffe
        San Ramón
        Sidikalang
        '''
        pass

    @abstractclassmethod
    def is_have_milk():
        '''which returns True / False in case there is a
        drinks milk or it is absent'''
        pass

    @property
    def size(self):
        return self.__size

    @property
    def name(self):
        return self.__name

    @property
    def milk(self):
        return self.__milk

    @property
    def to_go(self):
        return 'to go' if self.__to_go else 'on board'

    @size.setter
    def size(self, volume):
        if volume in ("litle", "medium", "big"):
            self.__size = volume
        else:
            raise ValueError("Value size is not valid!")

    @name.setter
    def name(self, volume):
        if volume in Coffee.names_of_coffee:
            self.__name = volume
        else:
            raise ValueError("Value name is not valid!")

    @milk.setter
    def milk(self, volume):
        if isinstance(volume, bool):
            self.__milk = volume
        else:
            raise ValueError("Value milk is not valid!")

    @to_go.setter
    def to_go(self, volume):
        if isinstance(volume, bool):
            self.__to_go = volume
        else:
            raise ValueError("Value 'to go' is not valid!")

    def __str__(self) -> str:
        return '\n'.join([
            self.get_cup_size(),
            self.coffee_name(),
            self.is_have_milk(),
            self.to_go
        ])
