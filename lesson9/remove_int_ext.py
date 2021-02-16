def remove_int_ext(values_list, num):
    conter = 0
    while num in values_list:
        values_list.remove(num)
        conter += 1
    return conter


list_val = [2, 3, 4, 5, 6, 5, 57, 8]
print(list_val)
print(remove_int_ext(list_val, 5))
print(list_val)
