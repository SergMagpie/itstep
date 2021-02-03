rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                  'violet']
user_color = input('Please input color with  red, orange, yellow,\
 green, blue, indigo or violet: ')
if user_color in rainbow_colors:
    index = rainbow_colors.index(user_color)

    print(rainbow_colors[index-1] if index > 1 else '',
          user_color, rainbow_colors[index+1] if index < 6 else '')
else:
    print('You make mistake')
