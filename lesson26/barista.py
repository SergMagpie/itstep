from latte import Latte
from cappuccino import Cappuccino
from black import Black
from espresso import Espresso
from mocha import Mocha


class Waiter:
    varieties = {'latte': Latte,
                 'cappuccino': Cappuccino,
                 'black': Black,
                 'espresso': Espresso,
                 'mocha': Mocha,
                 }

    @staticmethod
    def make_an_order(variety, size, name, milk, to_go):
        if variety.lower() in Waiter.varieties:
            return Waiter.varieties[variety.lower()](size, name, milk, to_go)
        else:
            raise ValueError('You were wrong with the choice of coffee')


def choose(dict_for_choose: dict) -> str:
    while True:
        key = input('Make your choose ')
        if key in dict_for_choose:
            return dict_for_choose[key]
        else:
            print('You made a mistake!')


def barista():
    list_of_orders = []
    sizes = {'1': "litle",
             '2': "medium",
             '3': 'big'}
    names = {'1': 'Arabica',
             '2': 'Robusta',
             '3': 'Liberica',
             '4': 'Excelsa',
             '5': 'Typica',
             '6': 'Kona',
             '7': 'Java',
             '8': 'Jamaican Blue Mountain',
             '9': 'Sumatra',
             '10': 'Bergendal',
             '11': 'Rume Sudan',
             '12': 'Amarello de Botancatú',
             '13': 'Blawan Paumah',
             '14': 'Java Mocha',
             '15': 'Pluma Hidalgo',
             '16': 'Creole',
             '17': 'Ethiopian Harrar',
             '18': 'Blue Mountain',
             '19': 'Villa Sarchi',
             '20': 'Ethiopian Sidamo',
             '21': 'Ethiopian Yiragacheffe',
             '22': 'San Ramón',
             '23': 'Sidikalang'
             }
    varieties = dict((str(i + 1), j) for i, j in enumerate(Waiter.varieties))
    while True:
        print("Greetings!")
        print("Would you like to have a cup of coffee?")
        if input('y/n ') == 'n':
            print('Goodbye!')
            break
        print('Enter, what variety of coffee do you like?')
        print("\n".join("'{}' - {}".format(
              k, v) for k, v in varieties.items()))
        variety = choose(varieties)
        print("Enter, what size matters?")
        print("\n".join("'{}' - {}".format(k, v) for k, v in sizes.items()))
        size = choose(sizes)
        print('Enter which coffee beans do you prefer?')
        print("\n".join("'{}' - {}".format(k, v) for k, v in names.items()))
        name = choose(names)
        milk = True
        if input('Add milk? y/n ') == 'n':
            milk = False
        to_go = True
        if input('To go? y/n ') == 'n':
            to_go = False
        list_of_orders.append(Waiter.make_an_order(
            variety, size, name, milk, to_go))
        print('In order', *list_of_orders, sep='\n')


if __name__ == "__main__":
    barista()
