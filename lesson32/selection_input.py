from base import Session
from cellphones import Phone
from processor import Processor


def my_print(strings):
    for i, j in strings:
        i = '\n'.join(str(i).split('\n')[:-2])
        j = '\n'.join(str(j).split('\n')[2:])
        print(i, 'has a processor', j, sep='\n')


session = Session()


def selection_input_1():
    try:
        lower_price = int(input('Enter lower price > '))
        top_price = int(input('Enter top price > '))
    except ValueError:
        print('You made a mistake')
    my_print(session.query(Phone, Processor).join(
        Processor, Phone.processor == Processor.id).filter(
        Phone.price > lower_price, Phone.price < top_price))


def selection_input_2():
    manufacturer = input('Enter manufacter name > ')
    my_print(session.query(Phone, Processor).join(
        Processor, Phone.processor == Processor.id).filter(
        Phone.company_manufacturer == manufacturer))


def selection_input_3():
    print(session.query(Phone).count())


def selection_input_4():
    my_print(session.query(Phone, Processor).join(
        Processor, Phone.processor == Processor.id))


key = None
while key != '0':
    print("""For display all phones in the price range they have\n\
to enter from the keyboard press 1\n\
For display all phones by company name\
produces press 2\n\
For number of phones in the table
from sqlalchemy import select press 3\n\
For display all phones press 4\n\
Press 0 for exit""")
    key = input('> ')
    if key == '1':
        selection_input_1()
    elif key == '2':
        selection_input_2()
    elif key == '3':
        selection_input_3()
    elif key == '4':
        selection_input_4()
