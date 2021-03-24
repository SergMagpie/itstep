class Human():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = None
        self.phone_number = None

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_phone_number(self):
        return self.phone_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def greetings(self):
        print("Hello, I'm {} {}!".format(self.last_name, self.first_name))

    def contact_info(self):
        print("My phone {}".format(self.phone_number))

vasa = Human('Vasya', "Ivanovich")
vasa.greetings()