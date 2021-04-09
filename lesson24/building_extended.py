from building import Building

from apartment import Apartment


class BuildingExtended(Building):
    '''Added methods for counting the number
    apartments, the number of people living in the house and
    adding a new apartment to the house.
    '''

    def __init__(self,
                 name: str,
                 number_of_floors: str,
                 height_of_the_building: str,
                 area: str,
                 city: str,
                 ) -> None:
        super().__init__(name, number_of_floors, height_of_the_building, area, city)
        self.__flats = []

    def counting_the_number_apartments(self) -> str:
        '''
        methods for counting the number apartments
        and return number or message about empty
        '''
        if self.__flats:
            return str(len(self.__flats))
        else:
            return f'Building {self.name} is empty.'

    def number_of_people(self) -> str:
        if self.__flats:
            count = 0
            for flat in self.__flats:
                count += int(flat.number_of_residential_apartments)
            return str(count)
        else:
            return f'Building {self.name} is empty.'

    def add_flat(self,
                 apartment_number: str,
                 number_of_residential_apartments: str,
                 floor: str,
                 area_of_apartments: str) -> None:
        self.__flats.append(Apartment(apartment_number,
                                      number_of_residential_apartments,
                                      floor,
                                      area_of_apartments))


if __name__ == "__main__":
    bild1 = BuildingExtended('Thower', '5', '15', '300', 'Kyiv')
    bild2 = BuildingExtended('Centre', '6', '17', '800', 'Odessa')
    print(bild1.name)
    print(bild1.number_of_floors)
    print(bild1.height_of_the_building)
    print(bild1.area)
    print(bild1.city)
    bild1.city = 'Riga'
    print(bild1.city)
    bild1.add_flat('1', '4', '2', '100')
    bild1.add_flat('2', '5', '3', '150')
    bild1.add_flat('3', '3', '4', '60')
    print(bild1.counting_the_number_apartments())
    print(bild2.counting_the_number_apartments())
    print(bild1.number_of_people())
    print(bild2.number_of_people())
