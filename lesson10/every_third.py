import even_list_generate


def every_third(start, finish):
    return even_list_generate.even_list_generate(start, finish)[::3]


if __name__ == "__main__":
    print(every_third(1, 9))
    print(every_third(2, 11))
    print(every_third(2, 10))
    print(every_third(0, 10))
    print(every_third(-6, 21))
    print(every_third(-6, -11))
