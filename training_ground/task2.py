def draw_a_pyramid(input_string: str) -> str:
    symbol, number = input_string.separate(' ')
    number = int(number)
    string = ''
    for i in range(1, number + 1):
        string += ' ' * (number - i) + symol * i + '\n'
    return str(len(string)) + '\n' + string

if __name__ == '__main__':
    print(draw_a_pyramid(input()))
