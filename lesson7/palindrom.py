string = input('Please enter a string and i \
will check if it is a palindrome or not: ').lower()
print(['No, your string is not a palindrom!',
       'Congratulations! Your string is a palindrome!']
      [[i for i in string if i != ' '] ==
       [i for i in string[::-1] if i != ' ']])
