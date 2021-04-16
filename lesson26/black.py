from coffee import Coffee


class Black(Coffee):
    def __init__(self, size, name, milk, to_go) -> None:
        super().__init__(size, name, milk, to_go)

    def get_cup_size(self):
        '''returns the size of a cup of coffee'''
        return f"Your Black is {self.size}"

    def coffee_name(self):
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
        return f"Your Black made with {self.name} beans"

    def is_have_milk(self):
        '''which returns True / False in case there is a
        drinks milk or it is absent'''
        return ("Your Black made " +
                f"{'with' if self.milk else 'without'} milk")
