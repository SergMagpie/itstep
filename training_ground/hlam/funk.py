def input_a_b(a, b):
    def sum_a_b(a, b):
        return a + b
    return sum_a_b(a, b) + 5


print(input_a_b(5, 3))