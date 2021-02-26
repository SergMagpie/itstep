import random
from functools import reduce

# создаем тренировочный полигон
the_matrix = []
for _ in range(100):
    row = []
    for _ in range(100):
        row.append(random.randint(-10000, 10000))
    the_matrix.append(row)
the_num = random.randint(0, 100)
# print(the_matrix)
# print(the_num)

# пишем человеческую функцию для проверки


def counter(matrix: list, num_of_string: int) -> int:
    count_string = 0
    for string in matrix:
        count_elem = 0
        for item in matrix[num_of_string]:
            if item in string:
                count_elem += 1
                if count_elem > 1:
                    count_string += 1
                    break
    return count_string


# изображаем решение Вашей задачи
count = len(list(filter(lambda k: len(k) > 1, list(
    map(lambda i: list(filter(lambda j: j in i, the_matrix[the_num])),
        the_matrix)))))

# сравниваем результаты
print(count)
print(counter(the_matrix, the_num))
# в условии не понятно, что делать с повторяющимися элементами,
# тут они задваиваются, если их нужно будет убрать, задачка упростится
