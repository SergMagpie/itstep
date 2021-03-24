class city:
    def __init__(self):
        self.city_name = ''
        self.region_name = ''
        self.name_countries = ''
        self.number_of_inhabitants_in_the_city = ''
        self.postal_code_area = ''
        self.telephone_area_code = ''

    def data_input(self):
        self.city_name = input('Enter city name ')
        self.region_name = input('Enter region name ')
        self.name_countries = input('Enter name countries ')
        self.number_of_inhabitants_in_the_city = input(
            'Enter number of inhabitants in the city ')
        self.postal_code_area = input('Enter postal code area ')
        self.telephone_area_code = input('Enter telephone area code ')

    def view_data(self):
        print('City name', self.city_name)
        print('Region name', self.region_name)
        print('Name countries', self.name_countries)
        print('Number of inhabitants in the city',
              self.number_of_inhabitants_in_the_city)
        print('Postal code area', self.postal_code_area)
        print('Telephone area code', self.telephone_area_code)


if __name__ == "__main__":
    c1 = city()
    c1.data_input()
    print()
    c1.view_data()
