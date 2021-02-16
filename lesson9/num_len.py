def num_len(num=''):
    if is_number(str(num)):
        return len([i for i in str(num) if i.isdigit()])
    else:
        print('you passed not a number to the function num_len()')
        return None


'''it was impossible to connect modules,
but there was no prohibition to steal a function'''


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


print(num_len(47589))
print(num_len(-47589))
print(num_len(-4758.9))
print(num_len(0))
print(num_len())
print(num_len('454738'))
print(num_len('454.738'))
print(num_len('-454.738'))
print(num_len('-45f4.738'))
print(num_len('-45 4.738'))
print(num_len('ftkgy'))
