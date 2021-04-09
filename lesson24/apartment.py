class Apartment:
    def __init__(self,
                 apartment_number: str,
                 number_of_residential_apartments: str,
                 floor: str,
                 area_of_apartments: str,
                 ) -> None:
        self.apartment_number = apartment_number
        self.number_of_residential_apartments = number_of_residential_apartments
        self.floor = floor
        self.area_of_apartments = area_of_apartments

    @property
    def apartment_number(self):
        return self.__apartment_number

    @property
    def number_of_residential_apartments(self):
        return self.__number_of_residential_apartments

    @property
    def floor(self):
        return self.__floor

    @property
    def area_of_apartments(self):
        return self.__area_of_apartments

    @apartment_number.deleter
    def apartment_number(self):
        del self.__apartment_number

    @number_of_residential_apartments.deleter
    def number_of_residential_apartments(self):
        del self.__number_of_residential_apartments

    @floor.deleter
    def floor(self):
        del self.__floor

    @area_of_apartments.deleter
    def area_of_apartments(self):
        del self.__area_of_apartments

    @apartment_number.setter
    def apartment_number(self, value) -> None:
        if value.isdigit():
            self.__apartment_number = value
        else:
            raise ValueError("Value must be a string and valid!")

    @number_of_residential_apartments.setter
    def number_of_residential_apartments(self, value) -> None:
        if value.isdigit():
            self.__number_of_residential_apartments = value
        else:
            raise ValueError("Value must be a string and valid!")

    @floor.setter
    def floor(self, value) -> None:
        if value.isdigit():
            self.__floor = value
        else:
            raise ValueError("Value must be a string and valid!")

    @area_of_apartments.setter
    def area_of_apartments(self, value) -> None:
        if value.isdigit():
            self.__area_of_apartments = value
        else:
            raise ValueError("Value must be a string and valid!")
