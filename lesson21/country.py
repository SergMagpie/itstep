import re


class Country():
    def __init__(self, name_of_the_country: str) -> None:
        self.name_of_the_country = name_of_the_country
        self.name_of_the_capital = ''
        self.continent = ''
        self.population_countries = ''
        self.names_of_cities = []

    def put_name_of_the_capital(self, name: str) -> None:
        if name.istitle():
            self.name_of_the_capital = name
        else:
            print("You made mistake!")

    def put_continent(self, name: str) -> None:
        if name in ("Asia",
                    "Africa",
                    "North America",
                    "South America",
                    "Antarctica",
                    "Europe",
                    "Australia",
                    "Eurasia",
                    "America"):
            self.continent = name
        else:
            print("You made mistake!")

    def put_population_countries(self, name: str) -> None:
        if re.fullmatch(r'\d+(?:[,.]\d*)*', name):
            self.population_countries = name
        else:
            print("You made mistake!")

    def put_names_of_cities(self, name: str) -> None:
        if name.istitle():
            self.names_of_cities.append(name)
        else:
            print("You made mistake!")


if __name__ == "__main__":
    def main():
        '''
        >>> u = Country('Ukraine')
        >>> u.name_of_the_country
        'Ukraine'
        >>> u.name_of_the_capital
        ''
        >>> u.put_name_of_the_capital('Kyiv')
        >>> u.name_of_the_capital
        'Kyiv'
        >>> u.put_name_of_the_capital('yiv')  
        You made mistake!
        >>> u.name_of_the_capital
        'Kyiv'
        >>> u.put_continent('Europ')
        You made mistake!
        >>> u.put_continent('Europe') 
        >>> u.continent
        'Europe'
        >>> u.put_population_countries('48bln')
        You made mistake!
        >>> u.put_population_countries('48 000 000') 
        You made mistake!
        >>> u.put_population_countries('48000000')   
        >>> u.population_countries                
        '48000000'
        >>> u.put_names_of_cities('Odessa')
        >>> u.put_names_of_cities('ochakov') 
        You made mistake!
        >>> u.put_names_of_cities('Ochakov') 
        >>> u.names_of_cities               
        ['Odessa', 'Ochakov']
        '''
        pass
    import doctest
    doctest.testmod()

    '''
PS D:\itstep> & C:/Users/sergm/AppData/Local/Programs/Python/Python39/python.exe d:/itstep/lesson21/country.py -v
Trying:
    u = Country('Ukraine')
Expecting nothing
ok
Trying:
    u.name_of_the_country
Expecting:
    'Ukraine'
ok
Trying:
    u.name_of_the_capital
Expecting:
    ''
ok
Trying:
    u.put_name_of_the_capital('Kyiv')
Expecting nothing
ok
Trying:
    u.name_of_the_capital
Expecting:
    'Kyiv'
ok
Trying:
    u.put_name_of_the_capital('yiv')
Expecting:
    You made mistake!
ok
Trying:
    u.name_of_the_capital
Expecting:
    'Kyiv'
ok
Trying:
    u.put_continent('Europ')
Expecting:
    You made mistake!
ok
Trying:
    u.put_continent('Europe')
Expecting nothing
ok
Trying:
    u.continent
Expecting:
    'Europe'
ok
Trying:
    u.put_population_countries('48bln')
Expecting:
    You made mistake!
ok
Trying:
    u.put_population_countries('48 000 000')
Expecting:
    You made mistake!
ok
Trying:
    u.put_population_countries('48000000')
Expecting nothing
ok
Trying:
    u.population_countries
Expecting:
    '48000000'
ok
Trying:
    u.put_names_of_cities('Odessa')
Expecting nothing
ok
Trying:
    u.put_names_of_cities('ochakov')
Expecting:
    You made mistake!
ok
Trying:
    u.put_names_of_cities('Ochakov')
Expecting nothing
ok
Trying:
    u.names_of_cities
Expecting:
    ['Odessa', 'Ochakov']
ok
7 items had no tests:
    __main__
    __main__.Country
    __main__.Country.__init__
    __main__.Country.put_continent
    __main__.Country.put_name_of_the_capital
    __main__.Country.put_names_of_cities
    __main__.Country.put_population_countries
1 items passed all tests:
  18 tests in __main__.main
18 tests in 8 items.
18 passed and 0 failed.
Test passed.
'''
