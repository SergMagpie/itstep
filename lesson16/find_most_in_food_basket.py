def find_most_in_food_basket(food_basket: dict, max_cost=True) -> set:
    '''
    Returns a set with the names of the cheapest or
    the most expensive products.
    >>> big_basket = {"bread": 1.2, "milk": 1.6, \
        "potato": 0.4, "sunflower oil": 2, "meat": 2.4, \
        "eggs": 0.4, "fish": 2.4}
    >>> find_most_in_food_basket(big_basket) == {'meat', 'fish'}
    True
    >>> find_most_in_food_basket(big_basket, max_cost=False) == {'eggs', 'potato'}
    True
    '''
    price = list(food_basket.values())
    price.sort(reverse=max_cost)
    return set([i for i in food_basket if food_basket[i] == price[0]])


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
PS D:\itstep> & C:/Users/sergm/AppData/Local/Programs/Python/Python39/python.exe d:/itstep/lesson16/find_most_in_food_basket.py -v
Trying:
    big_basket = {"bread": 1.2, "milk": 1.6,         "potato": 0.4, "sunflower oil": 2, "meat": 2.4,         "eggs": 0.4, "fish": 2.4}     
Expecting nothing
ok
Trying:
    find_most_in_food_basket(big_basket) == {'meat', 'fish'}
Expecting:
    True
ok
Trying:
    find_most_in_food_basket(big_basket, max_cost=False) == {'eggs', 'potato'}
Expecting:
    True
ok
1 items had no tests:
    __main__
1 items passed all tests:
   3 tests in __main__.find_most_in_food_basket
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
PS D:\itstep> """
