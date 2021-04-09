class Building:
    def __init__(self,
                 name: str,
                 number_of_floors: str,
                 height_of_the_building: str,
                 area: str,
                 city: str
                 ) -> None:
        self.name = name
        self.number_of_floors = number_of_floors
        self.height_of_the_building = height_of_the_building
        self.area = area
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def number_of_floors(self):
        return self.__number_of_floors

    @property
    def height_of_the_building(self):
        return self.__height_of_the_building

    @property
    def area(self):
        return self.__area

    @property
    def city(self):
        return self.__city

    @name.deleter
    def name(self):
        del self.__name

    @number_of_floors.deleter
    def number_of_floors(self):
        del self.__number_of_floors

    @height_of_the_building.deleter
    def height_of_the_building(self):
        del self.__height_of_the_building

    @area.deleter
    def area(self):
        del self.__area

    @city.deleter
    def city(self):
        del self.__city

    @name.setter
    def name(self, value: str) -> None:
        if value.istitle():
            self.__name = value
        else:
            raise ValueError("Value must be a string and valid!")

    @number_of_floors.setter
    def number_of_floors(self, value: str) -> None:
        if value.isdigit():
            self.__number_of_floors = value
        else:
            raise ValueError("Value must be a string and valid!")

    @height_of_the_building.setter
    def height_of_the_building(self, value: str) -> None:
        if value.isdigit():
            self.__height_of_the_building = value
        else:
            raise ValueError("Value must be a string and valid!")

    @area.setter
    def area(self, value: str) -> None:
        if value.isdigit():
            self.__area = value
        else:
            raise ValueError("Value must be a string and valid!")

    @city.setter
    def city(self, value: str) -> None:
        if value.istitle():
            self.__city = value
        else:
            raise ValueError("Value must be a string and valid!")
