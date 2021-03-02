def handbook():

    id_codes = []
    tel_numbers = []

    def sort_by_id():
        base = list(zip(id_codes, tel_numbers))
        base.sort(key=lambda x: x[0])
        for n, [i, j] in enumerate(base):
            id_codes[n] = i
            tel_numbers[n] = j
        print('The handbook is sorted by ID')

    def sort_by_phone_numbers():
        base = list(zip(id_codes, tel_numbers))
        base.sort(key=lambda x: x[1])
        for n, [i, j] in enumerate(base):
            id_codes[n] = i
            tel_numbers[n] = j
        print('The handbook is sorted by telephone numbers')

    def display_a_list_of_users():
        string_number = 0
        while string_number < len(id_codes):
            print(id_codes[string_number], tel_numbers[string_number])
            if not (string_number + 1) % 20:
                if input('Next screen? y/n ') == 'n':
                    break
            string_number += 1
        hello_screen()

    def make_items():
        def make_num(dig_cont: int) -> int:
            rez = []
            for i in range(dig_cont):
                j = str(int(i * 3.1415 * (length + i)
                            * (item + 1) * dig_cont) % 10)
                if not (i and int(j)):
                    j = '9'
                rez.append(j)
            return int(''.join(rez))
        while True:
            inp_len = input('Enter lengh a random handbook please ')
            if inp_len.isdecimal():
                length = int(inp_len)
                if length > 0:
                    id_codes.clear()
                    tel_numbers.clear()
                    for item in range(length):
                        tel_numbers.append(make_num(7))
                        id_codes.append(make_num(10))
                    print('The handbook is filled with random numbers')
                    return None
                else:
                    print('You made a mistake, enter a positive number')
            else:
                print('You made a mistake, enter a number')

    def insert_items():
        def input_digit(digit_capacity):
            while True:
                number = input(f'Enter a {digit_capacity}-digit' +
                               'the first digit is not zero ')
                if number.isdigit():
                    if len(number) == digit_capacity:
                        if number[0] != '0':
                            print('Number accepted')
                            return int(number)
                        else:
                            print('The first digit must be not zero')
                    else:
                        print(f'Number must be {digit_capacity}-digit')
                else:
                    print('Number must be number')
        id_code = input_digit(10)
        tel_number = input_digit(7)
        id_codes.append(id_code)
        tel_numbers.append(tel_number)

    def good_bye():
        print('Goodbye, I hope you enjoyed it')

    def hello_screen():
        print("Accept my congratulations!\nI'm a handbook.py program",
              "and I know how to manage a directory!",
              "If you press 'M', I will create a random handbook to test.",
              "You also have the ability to create your own dictionary,",
              "adding entries to it is possible with the 'I' key",
              "Sort by identification codes enter 'S'",
              "Sort by phone numbers enter 'P'",
              "Display a list of users with codes and phone numbers enter 'D'",
              sep='\n')

    rules = {
        'm': make_items,
        'i': insert_items,
        's': sort_by_id,
        'p': sort_by_phone_numbers,
        'd': display_a_list_of_users,
        'exit': good_bye,
    }
    key = ''
    hello_screen()
    while key != 'exit':
        key = input('Enter please M, I, S, P, D or exit for exit ').lower()
        if key in rules:
            rules[key]()
        else:
            print('Make your choice')


if __name__ == "__main__":
    handbook()
