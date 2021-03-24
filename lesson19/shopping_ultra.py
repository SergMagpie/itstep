
def shopping_list():
    import json
    '''
    Pprovide the ability to add new lists, 
    delete existing ones, find the most expensive and cheapest shopping list,
    read data on the first login from the file (where the data is serialized) 
    and after completion serialize and save to a file
    '''
    def create_new_shopping_list():
        shopping_list_example = [
            {
                "bread": 1.2,
                "milk": 1.6,
                "potato": 0.4,
                "sunflower oil": 2,
                "meat": 2.4
            },
            {
                "bread": 1.2,
                "milk": 1.6,
                "potato": 0.4,
                "sunflower oil": 2,
                "meat": 2.4,
                "eggs": 0.4,
                "fish": 2.4
            }
        ]
        with open("shopping_list_ultra.json", "a") as f_json:
            json.dump(shopping_list_example, f_json)
        return shopping_list_example

    def write_list(shopping_list: list, filename='shopping_list_ultra.json'):
        """
        Function for write list.
        """
        with open(filename, "w") as f:
            json.dump(shopping_list, f)

    def read_list(filename='shopping_list_ultra.json') -> list:
        """
        Function for read list.
        """
        try:
            with open(filename, "r") as f:
                shopping_list = json.load(f)

        except FileNotFoundError:
            key = input('The file is damaged. Create a new file? y/n ')
            if key == 'y':
                shopping_list = create_new_shopping_list()
            else:
                shopping_list = []
        return shopping_list

    def enter_the_cost():
        while True:
            cost = input('Enter the cost of the product: ')
            try:
                cost = float(cost)
                return cost
            except ValueError:
                print('You made mistake')

    def add_a_new_task():
        key = 'y'
        list_of_products = {}
        while key == 'y':
            task = input('\nEnter the product name: ')
            cost = enter_the_cost()
            list_of_products[task] = cost
            print('Produkt added')
            key = input('Add enother produkt? y/n ')

        shopping_list.append(list_of_products)
        print('List added')

    def delete_the_list():
        if shopping_list:
            num = input('\nEnter a number of list for deleting ')
            if num.isdigit():
                num = int(num) - 1
                if 0 <= num < len(shopping_list):
                    key = input(
                        'Are you sure deleted list: {} ? y/n '.format(shopping_list[num]))
                    if key == 'y':
                        del shopping_list[num]
                        print('List deleted')
                else:
                    print('You made mistake')
            else:
                print('You made mistake')
        else:
            print("\nShopping list is empty")

    def view_the_list():
        if shopping_list:
            print('\nYour tasks:')
            for n, i in enumerate(shopping_list):
                print('\nList number {}:'.format(n + 1))
                for j in i:
                    print(j, shopping_list[n][j])
        else:
            print("\nShopping list is empty")

    def vew_expencive_list(chipest=True):
        if shopping_list:
            indicator = ["chipest", "most expensive"][chipest]
            print('\nThe {} lists of products:'.format(indicator))
            prices = []
            for n, i in enumerate(shopping_list):
                price = 0
                for j in i:
                    price += shopping_list[n][j]
                prices.append((n, price))
            prices.sort(key=lambda x: x[1])
            extrim_price = prices[0 - chipest][1]
            list_task = [i[0] for i in prices if i[1] == extrim_price]
            for n in list_task:
                print('\nList number {} is the {}:'.format(n + 1, indicator))
                for j in shopping_list[n]:
                    print(j, shopping_list[n][j])
        else:
            print("\nShopping list is empty")

    def vew_cheapest_list():
        vew_expencive_list(chipest=False)

    def good_by():
        print('Good by! See you later!')
        write_list(shopping_list)

    shopping_list = read_list()

    box = {
        "a": add_a_new_task,
        "d": delete_the_list,
        "v": view_the_list,
        "e": vew_expencive_list,
        "c": vew_cheapest_list,
        "exit": good_by,
    }

    key = ''
    while key != 'exit':
        print("\nHello I'm your shopping list")
        print("Enter A for add a new list")
        print("Enter D for delete the list")
        print("Enter V for view the list")
        print("Enter E for view the most expensive list of products")
        print("Enter C for view the cheapest list of products")
        print("Enter EXIT for exit")
        key = input("Make your choice: ").lower()
        if key in box:
            box[key]()
        else:
            print('You made mistake')


if __name__ == "__main__":
    import os
    # Actualised a directory with a script.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    shopping_list()
