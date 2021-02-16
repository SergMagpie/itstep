def remove_int(values_list, num):
    return [i for i in values_list if i != num]


print(remove_int([4, 5, 6, 7], 5))
print(remove_int([4, 5, 6, 7, 'fdsf', 'dsfdsf'], 'fdsf'))
