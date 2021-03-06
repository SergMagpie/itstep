def company_user_base():
    '''
    Creates a company user base, 
    allows you to add users 
    and display a list of all added.
    '''
    import re
    data = []

    def input_str(mask: str, invitation: str) -> str:
        while True:
            string = input('Enter ' + invitation + ' ')
            if re.fullmatch(mask, string):
                return string
            else:
                print('You made mistake, try one more')

    def add_task():
        print("There must be 5 main fields" +
              "(Surname, Name, Position, " +
              "Phone number and e-mail address)")
        surname = input_str(r"[A-Z]\w+'?\w*", 'surname')
        name = input_str(r"[A-Z]\w+'?\w*", 'name')
        position = input_str(r".+", 'position')
        phone_number = input_str("\+380[-\s]?\d{2}[-\s]?\d{3}[-\s]?\d{4}",
                                 'phone_number +380-XX-XXX-XXXX')
        e_mail_address = input_str(r"[\w.-]+@[\w.-]+.\w+",
                                   'e_mail_address')
        data.append({
            'surname': surname,
            'name': name,
            'position': position,
            'phone_number': phone_number,
            'e_mail_address': e_mail_address,
        })

    def vew_task():
        for num, record in enumerate(data):
            print('\nRecord number ', num + 1)
            for field in record:
                print(field.capitalize(), '-', record[field])

    def delete_task():
        num = input('What number of record do you wont to delete? ')
        if num.isdigit():
            num = int(num)
            if 0 < num <= len(data):
                print('You choose fo delete record nuvber', num)
                for field in data[num - 1]:
                    print(field.capitalize(), '-', data[num - 1][field])
                key = input('Do you realy want to delete this record? y/n')
                if key == 'y':
                    del data[num - 1]
                    print('Record deleted')
            else:
                print('You made mistake')
        else:
            print('You made mistake')

    def good_by():
        print('Good by! See you later!')

    box = {'a': add_task,
           'v': vew_task,
           'd': delete_task,
           'exit': good_by,
           }

    key = ""
    while key != 'exit':
        print("\nHello, I'm a company user base!")
        print("Add a user - A\nView users - V\nDelete user - D")
        print("Exit for exit")
        key = input("Make your choice: ").lower()
        if key in box:
            box[key]()
        else:
            print('You make mistake')


if __name__ == "__main__":
    company_user_base()
