import calendar
# I could fit everything in three lines,
# but as Tim Peters said,
# "Beautiful is better than ugly!"
try:
    print(calendar.month_name[int(input()) or None])
except:
    print('You made a mistake, repeat with numbers from 1 to 12')
