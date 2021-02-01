rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                  'violet', 'red']
user_color = input(
    'Please input color with  red, orange, yellow, green, blue, indigo or violet: ')
if user_color in rainbow_colors:
    index = rainbow_colors.index(user_color)
    print(rainbow_colors[index-1],
          user_color, rainbow_colors[index+1])
else:
    print('You make mistake')