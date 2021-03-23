
def to_do_list():
    import json
    '''
    Key features:
    - The user can add a new task
    - the user can edit the task
    - the user can delete the task
    - the user can mark the task as completed
    - the user can view the list of completed and
    unfulfilled tasks and deduce to understand which of
    tasks has what status.
    '''
    def create_new_shopping_list():
        shoping_list_example = [
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
            json.dump(shoping_list_example, f_json)
        return shoping_list_example

    def write_list(shoping_list: list, filename='shopping_list_ultra.json'):
        """
        Function for write list.
        """
        with open(filename, "w") as f:
            json.dump(shoping_list, f)

    def read_list(filename='shopping_list_ultra.json') -> list:
        """
        Function for read list.
        File integrity check not implemented, if necessary,
        I can add a checksum. But this is not all today.
        """
        try:
            with open(filename, "r") as f:
                shoping_list = json.load(f)

        except FileNotFoundError:
            key = input('The file is damaged. Create a new file? y/n ')
            if key == 'y':
                shoping_list = create_new_shopping_list()
        return shoping_list

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

        shoping_list.append(list_of_products)
        print('List added')

    def delete_the_list():
        num = input('\nEnter a number of list for deleting ')
        if num.isdigit():
            num = int(num) - 1
            if 0 <= num < len(shoping_list):
                key = input(
                    'Are you sure deleted list: {} ? y/n '.format(shoping_list[num]))
                if key == 'y':
                    del shoping_list[num]
                    print('List deleted')
            else:
                print('You made mistake')
        else:
            print('You made mistake')

    def view_the_list():
        print('\nYour tasks:')
        for n, i in enumerate(shoping_list):
            print('\n{} list:'.format(n + 1))
            for j in i:
                print(j, shoping_list[n][j])

    def vew_expencive_list(chipest=False):
        indicator = ["most expensive","chipest"][chipest]
        print('\nThe {} list of products:'.format(indicator))
        prices = []
        for n, i in enumerate(shoping_list):
            price = 0
            for j in i:
                price += shoping_list[n][j]
            prices.append((n, price))
        prices.sort(key=lambda x: x[1])
        n = prices[0 - chipest][0]
        print('\n{} list the {}:'.format(n + 1, indicator))
        for j in shoping_list[n]:
            print(j, shoping_list[n][j])

    def vew_cheapest_list():
        vew_expencive_list(chipest=True)

    def good_by():
        print('Good by! See you later!')
        write_list(shoping_list)

    shoping_list = read_list()
    print(shoping_list)

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
        print("\nHello I'm your shoping list")
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
    to_do_list()
