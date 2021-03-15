def calculate_food_basket(food_basket: dict, exchange_rate: float) -> float:
    '''
    Receives a consumer basket with products and the cost of these
    products in conventional units presented as
    dictionary and exchange rate and returns the cost of all
    products for this course.    
    >>> calculate_food_basket({"bread": 1.2, "milk": 1.6, \
        "potato": 0.4, "sunflower oil": 2, "meat": 2.4}, 27.5)
    209.0
    '''
    return sum(map(lambda x: x * exchange_rate, food_basket.values()))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

'''
PS D:\itstep> & C:/Users/sergm/AppData/Local/Programs/Python/Python39/python.exe d:/itstep/lesson16/?calculate_food_basket?.py -v
Trying:
    calculate_food_basket({"bread": 1.2, "milk": 1.6,         "potato": 0.4, "sunflower oil": 2, "meat": 2.4}, 27.5)
Expecting:
    209.0
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.calculate_food_basket
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
PS D:\itstep> 
'''