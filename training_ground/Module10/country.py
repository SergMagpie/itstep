class country:
    def __init__(self):
        self.country_name = ''
        self.continent_name = ''
        self.number_of_inhabitants_in_the_country = ''
        self.country_phone_code = ''
        self.the_name_of_the_capital = ''
        self.the_name_of_the_countrys_cities = ''

    def data_input(self):
        self.country_name = input('Enter country name ')
        self.continent_name = input('Enter continent name ')
        self.number_of_inhabitants_in_the_country = input(
            'Enter number of inhabitants in the country ')
        self.country_phone_code = input('Enter country phone code ')
        self.the_name_of_the_capital = input('Enter the name of the capital ')
        self.the_name_of_the_countrys_cities = input(
            'Enter the name of the countrys cities ')

    def view_data(self):
        print('Country name ', self.country_name)
        print('Continent name ', self.continent_name)
        print('Number of inhabitants in the country ',
              self.number_of_inhabitants_in_the_country)
        print('Country phone code ', self.country_phone_code)
        print('The name of the capital ', self.the_name_of_the_capital)
        print('The name of the countrys cities ',
              self.the_name_of_the_countrys_cities)


if __name__ == "__main__":
    c1 = country()
    c1.data_input()
    print()
    c1.view_data()
