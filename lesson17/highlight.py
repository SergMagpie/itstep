def highlight(text: str, str_to_select: str, decoration: str) -> str:
    '''
    Accept a certain line with text,
    the line of what you want to highlight in the text 
    and the characters that highlight this text 
    on the left and right.
    >>> quote = "Guns. LOTS Of Guns."
    >>> highlight(quote, "Guns", "**")
    '**Guns**. LOTS Of **Guns**.'
    >>> highlight(quote, "guns", "**")
    'Guns. LOTS Of Guns.'
    '''
    import re
    return re.sub(str_to_select,
                  decoration + str_to_select + decoration,
                  text)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

'''
PS D:\itstep> & C:/Users/sergm/AppData/Local/Programs/Python/Python39/python.exe d:/itstep/lesson17/highlight.py -v
Trying:
    quote = "Guns. LOTS Of Guns."
Expecting nothing
ok
Trying:
    highlight(quote, "Guns", "**")
Expecting:
    '**Guns**. LOTS Of **Guns**.'
ok
Trying:
    highlight(quote, "guns", "**")
Expecting:
    'Guns. LOTS Of Guns.'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   3 tests in __main__.highlight
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
PS D:\itstep> 
'''
