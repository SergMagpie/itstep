def five_min(*in_values):
    if len(in_values) != 5:
        print(f'the function should have accepted 5 \
variables, you passed {len(in_values)}')
        return None
    elif all([type(i) == type(in_values[0]) for i in in_values[1:]]):
        min_val = in_values[0]
        for i in in_values[1:]:
            if min_val > i:
                min_val = i
        return min_val
    else:
        print('you passed variables of different types, \
they cannot be compared')
        return None


print(five_min(3, 5, 7, 2, 9))
print(five_min('3', '5', '7', '2', '9'))
print(five_min('3', '5', '7', '2'))
print(five_min('nhd', 'ngfd', 'ngfdn', 'ngfdn', 'vfvs'))
print(five_min('nhd', 'ngfd', 8, 'ngfdn', 'vfv'))
print(five_min())
