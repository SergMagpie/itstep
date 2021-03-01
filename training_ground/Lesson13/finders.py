def len_find(num, arcs):
    for n, i in enumerate(arcs):        
        if i == num:
            return n
    else:
        print('Number is empty')
        return -1


def bin_find(num, arcs, low=None, high=None):    
    if low == None or high == None:
        low = 0
        high = len(arcs) - 1
    if low < high:
        mid = (high + low) // 2
        if num == arcs[mid]:
            return mid
        elif num < arcs[mid]:
            return bin_find(num, arcs, low=low, high=mid - 1)
        else:
            return bin_find(num, arcs, low=mid + 1, high=high)
    else:
        print('Number is empty')
        return -1


if __name__ == "__main__":
    print(len_find(20, [5, 6, 8, 9, 7, 2, 3, 4, 20, 11]))
    print(len_find(20, [5, 6, 8, 9, 7, 2, 3, 4, 21, 11]))
    print(bin_find(15, [2, 3, 4, 6, 7, 8, 9, 11, 23, 54, 56, 88, 99]))
    print(bin_find(15, [2, 3, 4, 6, 7, 8, 9, 11, 15, 23, 54, 56, 88, 99]))
