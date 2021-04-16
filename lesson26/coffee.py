from abc import ABCMeta, abstractclassmethod


class Coffee(metaclass=ABCMeta):

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
