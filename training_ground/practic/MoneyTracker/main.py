from wallet import Wallet
from colorama import Fore, Back, Style
from datetime import date as d
from datetime import datetime

class ConsoleInterface:
    
    menu_keys = {"a", "s", "i", "o", "e"}

    def __init__(self, wallet):
        self.wallet = wallet()
        self.menu_keys_adv = {"a": self.add,
                              "s": self.show_all,
                              "i": self.income,
                              "o": self.outcome}

    @staticmethod
    def clean_style():
        print(Style.RESET_ALL, end='')
    
    @staticmethod
    def money_validator(value_str):
        val = None
        try:
            val = float(value_str)
        except ValueError:
            return None
        return val

    @staticmethod
    def date_validator(value_str):
        val = None
        try:
            if value_str == '':
                return d.today()
            val = datetime.strptime(value_str, "%Y/%m/%d")
            val = val.date()
        except ValueError:
            return None
        return val
    
    def input_field(self, ask_text, error_text, validation_method):
        while True:
            validated_data = validation_method(input(ask_text + " "))
            if validated_data is None:
                print(Fore.RED, error_text)
                self.clean_style()
            else:
                return validated_data
    
    def add(self):
        """Метод відповідає за додавання нового запису"""
        money_amount = self.input_field("Введіть кількість грошей", 
                                        "Введіть дані в форматі числа (приклад -20.5)",
                                        self.money_validator)
        transaction_date = self.input_field("Введіть дату коли було отримання/витрата коштів в форматі рік/місяць/день\nАбо натиснувши Enter і буде записано сьогоднішню дату",
                                            "Введіть дані в форматі дня (приклад 2021/5/3)",
                                            self.date_validator)
        self.wallet.new_record(money_amount, transaction_date)

    def show_all(self):
        print("show all")

    def income(self):
        print("show income")

    def outcome(self):
        print("show outcome")

    def menu(self):
        print(Fore.GREEN, "Menu:",
              "a - Add new record\n",
              "s - Show all\n",
              "i - income\n",
              "o - outcome\n",
              "e - for exit")
        self.clean_style()

    def start(self):
        while True:
            self.menu()
            key = input()
            if key not in self.menu_keys_adv and key != "e":
                print(f"{Fore.RED}You made mistake (;")
                self.clean_style()
            elif key == "e":
                break
            else:
                self.menu_keys_adv[key]()

if __name__ == "__main__":
    interface = ConsoleInterface(Wallet)
    interface.start()