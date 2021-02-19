def even_list_generate(start, finish):
    return list(range(start + 1 if start % 2 else start, finish + 1, 2))


if __name__ == "__main__":
    print(even_list_generate(1, 9))
    print(even_list_generate(2, 11))
    print(even_list_generate(2, 10))
    print(even_list_generate(0, 10))
    print(even_list_generate(-6, 11))
    print(even_list_generate(-6, -11))
