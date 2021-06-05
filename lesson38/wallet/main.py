from wallet import Wallet
from colorama import Fore, Back, Style
from datetime import datetime, timedelta, date as d


class ConsoleInterface:
    LAST_WEEK = (d.today() - timedelta(days=7), d.today())
    LAST_MONTH = ((d.today().replace(day=1) - timedelta(days=1)
                   ).replace(day=d.today().day), d.today())

    def __init__(self, wallet):
        self.wallet = wallet()
        self.menu_keys_adv = {"a": self.add,
                              "u": self.update,
                              "s": self.show_all,
                              "sw": self.show_all_for_last_week,
                              "sm": self.show_all_for_last_month,
                              "i": self.income,
                              "iw": self.show_income_for_last_week,
                              "im": self.show_income_for_last_month,
                              "o": self.outcome,
                              "ow": self.show_outcome_for_last_week,
                              "om": self.show_outcome_for_last_month,
                              "mo": self.get_the_most_expensive_costs,
                              "mi": self.get_main_source_of_income
                              }

    @staticmethod
    def clean_style():
        """Метод припиняє зміну кольору колорамою"""
        print(Style.RESET_ALL, end='')

    @staticmethod
    def money_validator(value_str):
        """Метод перевіряє правильність введення суми грошей"""
        val = None
        try:
            val = float(value_str)
        except ValueError:
            return None
        return val

    @staticmethod
    def int_validator(value_str):
        """Метод перевіряє правильність введення ID"""
        val = None
        try:
            val = int(value_str)
        except ValueError:
            return None
        return val

    @staticmethod
    def date_validator(value_str):
        """Метод перевіряж правильність введення дати"""
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
        """Метод перевіряє валідність введеної інформації 
        і повертає її валідною"""
        while True:
            validated_data = validation_method(input(ask_text + " "))
            if validated_data is None:
                print(Fore.RED, error_text)
                self.clean_style()
            else:
                return validated_data

    def add(self):
        """Метод відповідає за додавання нового запису"""
        money_amount = self.input_field(
            "Введіть кількість грошей",
            "Введіть дані в форматі числа (приклад -20.5)",
            self.money_validator)
        transaction_date = self.input_field(
            "Введіть дату коли було отримання/витрата коштів " +
            "в форматі рік/місяць/день" +
            "\nАбо натиснувши Enter і буде записано сьогоднішню дату",
            "Введіть дані в форматі дня (приклад 2021/5/3)",
            self.date_validator)
        reason = input('Введіть статтю транзакції ')
        contragent = input('Введіть контрагента транзакції ')
        self.wallet.new_record(money_amount,
                               transaction_date,
                               reason,
                               contragent)

    def show_all(self):
        """Метод відповідає за показ всіх записів"""
        records = self.wallet.get_all_records()
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def income(self):
        """Метод відповідає за показ всіх вхідних записів за період"""
        begin = self.input_field(
            "Введіть дату початку періоду в форматі рік/місяць/день" +
            "\nАбо натисіть Enter і буде записано сьогоднішню дату",
            "\nВведіть дані в форматі дня (приклад 2021/5/3)",
            self.date_validator)
        end = self.input_field(
            "Введіть дату кінця періоду в форматі рік/місяць/день" +
            "\nАбо натисіть Enter і буде записано сьогоднішню дату",
            "\nВведіть дані в форматі дня (приклад 2021/5/3)",
            self.date_validator)

        records = self.wallet.get_income(begin, end)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def outcome(self):
        """Метод відповідає за показ всіх вихідних записів за період"""
        begin = self.input_field(
            "Введіть дату початку періоду в форматі рік/місяць/день" +
            "\nАбо натисіть Enter і буде записано сьогоднішню дату",
            "\nВведіть дані в форматі дня (приклад 2021/5/3)",
            self.date_validator)
        end = self.input_field(
            "Введіть дату кінця періоду в форматі рік/місяць/день" +
            "\nАбо натисіть Enter і буде записано сьогоднішню дату",
            "\nВведіть дані в форматі дня (приклад 2021/5/3)",
            self.date_validator)

        records = self.wallet.get_outcome(begin, end)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def update(self):
        """Метод відповідає за редагування запису"""
        id_row = self.input_field(
            "Введіть ID запису для зміни",
            "Введіть дані в форматі числа (приклад 1)",
            self.int_validator)
        record = self.wallet.get_record_whith_id(id_row)
        if not record.count():
            if input(
                    'Такого запису не інснує, створити новий? y/n ') == 'y':
                self.add()
        else:
            print(*record)
            print('Change this record\n')
            money_amount = self.input_field(
                "Введіть кількість грошей",
                "Введіть дані в форматі числа (приклад -20.5)",
                self.money_validator)
            transaction_date = self.input_field(
                "Введіть дату коли було отримання/витрата коштів " +
                "в форматі рік/місяць/день" +
                "\nАбо натиснувши Enter і буде записано сьогоднішню дату",
                "Введіть дані в форматі дня (приклад 2021/5/3)",
                self.date_validator)
            reason = input('Введіть статтю транзакції ')
            contragent = input('Введіть контрагента транзакції ')
            self.wallet.update(id_row, {"money_amount": money_amount,
                                        "date": transaction_date,
                                        "reason": reason,
                                        "contragent": contragent})

    def show_all_for_last_week(self):
        records = self.wallet.get_all_records(*self.LAST_WEEK)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def show_all_for_last_month(self):
        records = self.wallet.get_all_records(*self.LAST_MONTH)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def show_income_for_last_week(self):
        records = self.wallet.get_income(*self.LAST_WEEK)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def show_income_for_last_month(self):
        records = self.wallet.get_income(*self.LAST_MONTH)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def show_outcome_for_last_week(self):
        records = self.wallet.get_outcome(*self.LAST_WEEK)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def show_outcome_for_last_month(self):
        records = self.wallet.get_outcome(*self.LAST_MONTH)
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def get_the_most_expensive_costs(self):
        records = self.wallet.get_the_most_expensive_costs()
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def get_main_source_of_income(self):
        records = self.wallet.get_main_source_of_income()
        if not records.count():
            records = ["There is no information",
                       "\non your request"]
        print(*records)

    def menu(self):
        """метод показує меню програми"""
        print(Fore.GREEN, "Menu:",
              "a - Add new record\n",
              "u - Update record\n",
              "s - Show all\n",
              "    sw - Show all for last week\n",
              "    sm - Show all for last month\n",
              "i - income\n",
              "    iw - Show income for last week\n",
              "    im - Show income for last month\n",
              "o - outcome\n",
              "    ow - Show outcome for last week\n",
              "    om - Show outcome for last month\n",
              "mo - Show the most expensive costs\n",
              "mi - Show main source of income\n",
              "e - for exit")
        self.clean_style()

    def start(self):
        """головний цикл програми"""
        while True:
            self.menu()
            key = input('> ')
            if key not in self.menu_keys_adv and key != "e":
                print(f"{Fore.RED}You made mistake (;")
                self.clean_style()
            elif key == "e":
                self.wallet.close()
                break
            else:
                self.menu_keys_adv[key]()


if __name__ == "__main__":
    interface = ConsoleInterface(Wallet)
    interface.start()
