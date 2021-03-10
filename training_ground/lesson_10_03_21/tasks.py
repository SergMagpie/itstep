# it is a task 3
def same_cities_upgrade(funk):
    def wrapper(first_traveler_cities, second_traveler_cities):
        key = ''
        while key != 'exit':
            key = input('Enter 1 or 2 for print cities first or second users,\
 3 for print same cities and exit for exit ')
            if key == '1':
                print(first_traveler_cities - second_traveler_cities)
            elif key == '2':
                print(second_traveler_cities - first_traveler_cities)
            elif key == '3':
                print(first_traveler_cities & second_traveler_cities)
            elif key == 'exit':
                print('Good buy')
            else:
                print('You made mistake')
        return funk(first_traveler_cities, second_traveler_cities)
    return wrapper


# it is a task 1, but task 3 it is wrapper for task 1
@ same_cities_upgrade
def same_cities(first_traveler_cities: set, second_traveler_cities: set) -> set:
    return first_traveler_cities & second_traveler_cities


mark_cities = {"Boston", "Lisbon", "Paris", "London"}
peter_cities = {"New York", "Lisbon", "Michigan", "London"}
print(same_cities(mark_cities, peter_cities))


# it is a task 2
def unique_ids(ids: list) -> list:
    return list(set(ids))


print(unique_ids([1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9, 8, 12, 13, 14, 14, 19]))
