def binary_search(num: int, arcs: list, low=None, high=None) -> int:
    '''
    The function finds the ordinal number of the element 
    in the ascending list of elements using a binary search algorithm 
    or returns -1 in its absence. num - an element to be found, 
    arcs - a list in which to look for it.
    '''
    # recursion check
    if low == None or high == None:
        low = 0
        high = len(arcs)
    # item search
    if low < high:
        mid = (high + low) // 2
        if num == arcs[mid]:
            return mid
        elif num < arcs[mid]:
            return binary_search(num, arcs, low=low, high=mid - 1)
        else:
            return binary_search(num, arcs, low=mid + 1, high=high)
    # item missing message
    else:
        return -1


if __name__ == "__main__":

    print(binary_search(2, [2, 3, 4, 6, 7, 8, 9, 11, 23, 54, 56, 88, 99]))
    print(binary_search(99, [2, 3, 4, 6, 7, 8, 9, 11, 15, 23, 54, 56, 88, 99]))
    print(binary_search(11, [2, 3, 4, 6, 7, 8, 9, 11, 15, 23, 54, 56, 88, 99]))
