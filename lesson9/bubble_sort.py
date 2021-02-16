def bubble_sort(num_list, reverse=False):
    sort_list = num_list.copy()
    n = len(sort_list)
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if reverse:
                if sort_list[j] < sort_list[j + 1]:
                    sort_list[j], sort_list[j +
                                            1] = sort_list[j + 1], sort_list[j]
                    flag = False
            else:
                if sort_list[j] > sort_list[j + 1]:
                    sort_list[j], sort_list[j +
                                            1] = sort_list[j + 1], sort_list[j]
                    flag = False
        if flag:
            break
    return sort_list


old_list = [4, 5, 7, 3, 2]
new_list = bubble_sort(old_list)
new_list_reverse = bubble_sort(old_list, True)
print(old_list)
print(new_list)
print(new_list_reverse)
