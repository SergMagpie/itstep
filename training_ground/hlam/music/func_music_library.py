def add(elem_name: str) -> list:
    '''
    Provides the ability to add an item. 
    Returns the list of values of the element.
    '''
    list_of_elem = []
    next_elem = True
    while next_elem:
        list_of_elem.append(input('Enter {} '.format(elem_name)))
        next_elem = input('Add next {}? y/n '.format(elem_name)) == 'y'
    return list_of_elem


def change(elem_name: str) -> list:
    '''
    Allows you to change the value of the item.
    Returns new list of values of element.
    '''
    list_of_elem = []
    next_elem = True
    while next_elem:
        list_of_elem.append(input('Change {} '.format(elem_name)))
        next_elem = input('Add next {}? y/n '.format(elem_name)) == 'y'
    return list_of_elem


def delete(elem_name: str) -> bool:
    '''
    Asks if the item should be deleted.
    If the answer YES returns the True 
    or a False if the answer is NO.
    '''
    return input('Delete {}? y/n '.format(elem_name)) == 'y'
