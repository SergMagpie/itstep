# объявление функции
def draw_box():
    print('*' * 10)
    for _ in range(10):
        print('*', ' ' * 6, '*')
    print('*' * 10)
# основная программа
draw_box()  # вызов функции