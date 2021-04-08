class Wallet:
    def __init__(self, owner_s_name, amount_of_money, currency_code) -> None:
        self.owner_s_name = owner_s_name
        self.amount_of_money = amount_of_money
        self.currency_code = currency_code

    def __str__(self) -> str:
        return ' '.join([self.owner_s_name, str(self.amount_of_money), self.currency_code])

    @property
    def owner_s_name(self):
        return self.__owner_s_name

    @owner_s_name.setter
    def owner_s_name(self, value: str):
        if value.istitle():
            self.__owner_s_name = value
        else:
            raise ValueError("Name must be upper case!")

    @owner_s_name.deleter
    def owner_s_name(self):
        del self.__owner_s_name

    @property
    def amount_of_money(self):
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: str):
        if value.isdigit():
            self.__amount_of_money = value
        else:
            raise ValueError("Name must be upper case!")

    @amount_of_money.deleter
    def amount_of_money(self):
        del self.__amount_of_money

    @property
    def currency_code(self):
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: str):
        if value in ['UAN', 'USD', 'EUR']:
            self.__currency_code = value
        else:
            raise ValueError("Currency code must be UAN, USD, EUR!")

    @currency_code.deleter
    def currency_code(self):
        del self.__currency_code

if __name__ == "__main__":
    lapatnik = Wallet('Serhii', '5000', 'UAN')
    print(lapatnik)
    moshna = Wallet('Alla', '10000', 'EUR')
    print(moshna)
    moshna.owner_s_name = 'Dima'
    print(moshna)
    del moshna.owner_s_name
    print(moshna)
