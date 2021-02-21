class human:
    count = 0

    def __init__(self):
        self.full_name = ''
        self.date_of_birth = ''
        self.contact_phone_number = ''
        self.city = ''
        self.country = ''
        self.home_address = ''
        human.count += 1

    @staticmethod
    def count_human():
        print(human.count)

    def data_input(self):
        self.full_name = input('Enter full name ')
        self.date_of_birth = input('Enter date of birth ')
        self.contact_phone_number = input('Enter contact phone number ')
        self.city = input('Enter city ')
        self.country = input('Enter country ')
        self.home_address = input('Enter home address ')

    def view_data(self):
        print('Full name', self.full_name)
        print('Date of birth', self.date_of_birth)
        print('Contact phone number', self.contact_phone_number)
        print('City', self.city)
        print('Country', self.country)
        print('Home address', self.home_address)


if __name__ == "__main__":
    h1 = human()
    h2 = human()
    h1.data_input()
    print()
    h1.view_data()
    h1.count_human()
    h2.count_human()
    human.count_human()
    print(human.count)
    print(dir(h1))
