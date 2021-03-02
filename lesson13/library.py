def library():
    books = []
    years = []

    def make_items():
        '''
        library obtained using the module itstep/training_ground/parce.py
        '''
        catalog = [
        ('Python и анализ данных', '2020'),
        ('Алгоритмы. Справочник с примерами на C, C++, Java и Python', '2020'),
        ('PYTHON для дітей. Веселий вступ до програмування', '2017'),
        ('Пришвидшений курс Python. Практичний, проєктно-орієнтований вступ до програмування', '2021'),
        ('Программирование на Python. Иллюстрированное руководство для детей', '2018'),
        ('Програмування мовою Python', '2019'),
        ('Python для детей. Самоучитель по программированию', '2017'),
        ('Программируем с Minecraft. Создай свой мир с помощью Python', '2019'),
        ('Python. Книга Рецептов', '2019'),
        ('Eric and the Pimple Potion', '2019'),
        ('The Gun Seller', '2004'),
        ('The Messenger', '2007'),
        ('Getting More', '2011'),
        ('Ukraine Diaries: Dispatches from Kiev', '2014'),
        ('Europe. A History', '2014'),
        ('Furious Hours: Murder, Fraud and the Last Trial of Harper Lee', '2019'),
        ("The President's Last Love", '2009'),
        ("The Skin I'm In", '2001'),
        ('Hellhound on his Trail', '2011'),
        ('Hate Mail', '2012'),
        ('The Unfinished Clue', '2007'),
        ('The Secrets We Kept', '2019'),
        ('Фаетон. Том 2. Повстання', '2019'),
        ('Exotic. A Fetish for the Foreign', '2019'),
        ('Nonstop', '2020'),
        ('The Design Book', '2020'),
        ('Whose Bones? An Animal Guessing Game', '2020'),
        ('Крихка імперія. Як Росія полюбила і розлюбила Владіміра Путіна ', '2015'),
        ('Зло. Розкриття сутності зла у літературі та мистецтві', '2015'),
        ('Хроніки Південного', '2019'),
        ('Від Холодної війни до Гарячого миру', '2021'),
        ('Після Путіна. Наступники, стабільність і майбутнє Росії ', '2021'),
        ('Искусственный интеллект с примерами на Python', '2019'),
        ('Python 3 и PyQt 5. Разработка приложений', '2019'),
        ('Машинное обучение с использованием Python. Сборник рецептов', '2020'),
        ('Coding for Beginners. Using Python', '2017'),
        ('Python для чайников', '2019'),
        ('Машинное обучение. Карманный справочник. Краткое руководство по методам структурированного машинного обучения на Python', '2020'),
        ('Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта', '2016'),
        ('Начинаем программировать на Python', '2019'),
        ('Криптография и взлом шифров на Python', '2019'),
        ('Computer Coding Python Games for Kids', '2018'),
        ('Python 3. Самое необходимое', '2020'),
        ('Глубокое обучение и TensorFlow для профессионалов. Математический подход к построению систем искусственного интеллекта на Python', '2020')
        ]
        for i, j in catalog:
            books.append(i)
            years.append(j)
        print('The lidrary is load!\nlibrary obtained using the module itstep/training_ground/parce.py',
        '\nwith https://www.yakaboo.ua/search/?multi=0&cat=&q=python')

    def sort_by_books():
        base = list(zip(books, years))
        base.sort(key=lambda x: x[0])
        for n, [i, j] in enumerate(base):
            books[n]=i
            years[n]=j
        print('The lidrary is sorted by books')

    def sort_by_years():
        base=list(zip(books, years))
        base.sort(key=lambda x: x[1])
        for n, [i, j] in enumerate(base):
            books[n]=i
            years[n]=j
        print('The library is sorted by years')

    def display_a_list_of_users():
        string_number=0
        while string_number < len(books):
            print(books[string_number], years[string_number])
            if not (string_number + 1) % 20:
                if input('Next screen? y/n ') == 'n':
                    break
            string_number += 1
        hello_screen()

    def insert_items():
        def input_digit(digit_capacity):
            while True:
                number=input(f'Enter a {digit_capacity}-digit' +
                               'the first digit is not zero ')
                if number.isdigit():
                    if len(number) == digit_capacity:
                        if number[0] != '0':
                            print('Number accepted')
                            return number
                        else:
                            print('The first digit must be not zero')
                    else:
                        print(f'Number must be {digit_capacity}-digit')
                else:
                    print('Number must be number')
        book=input('Enter a title of the book ')
        year=input_digit(4)
        books.append(book)
        years.append(year)

    def good_bye():
        print('Goodbye, I hope you enjoyed it')

    def hello_screen():
        print("Accept my congratulations!\nI'm a library.py program",
              "and I know how to manage a directory!",
              "If you press 'M', I will create a random library to test.",
              "You also have the ability to create your own library,",
              "adding entries to it is possible with the 'I' key",
              "Sort by books enter 'S'",
              "Sort by years enter 'P'",
              "Display a list of books whith years enter 'D'",
              sep='\n')

    rules={
        'm': make_items,
        'i': insert_items,
        's': sort_by_books,
        'p': sort_by_years,
        'd': display_a_list_of_users,
        'exit': good_bye,
    }
    key=''
    hello_screen()
    while key != 'exit':
        key=input('Enter please M, I, S, P, D or exit for exit ').lower()
        if key in rules:
            rules[key]()
        else:
            print('Make your choice')


if __name__ == "__main__":
    library()
