def main():

    def add_new_country():
        country = input('Enter country name ')
        capital = input('Enter capital name ')
        country_dict[country] = capital

    def remove_pair():
        dell = input('Enter name for dell ')
        name = ''
        for country, capital in country_dict.items():
            if dell in country or dell in capital:
                name = country
        if name:
            country_dict.pop(name)
        else:
            print('name for dell is wrong')

    def find_info():
        info = input('Enter find name ')
        listing = []
        for country, capital in country_dict.items():
            if info in country or info in capital:
                listing.append(country)
        for i in listing:
            print(i, '-->>', country_dict[i])

    def good_by():
        print('good by')

    country_dict = {}
    commands = {
        '1': add_new_country,
        '2': remove_pair,
        '3': find_info,
        'exit': good_by,
    }
    command = ''
    while command != 'exit':
        command = input(
            '1 - add new Country\n2 - remove pair\n3 - find info\nexit for exit ')
        if command in commands:
            commands[command]()
        else:
            print('You made mistake')


if __name__ == "__main__":
    main()
