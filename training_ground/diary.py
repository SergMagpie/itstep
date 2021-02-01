day_of_Week = ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday']
day_of_week = ['monday', 'tuesday', 'wednesday',
               'thursday', 'friday', 'saturday', 'sunday']
diary = {'Monday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 'Tuesday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 'Wednesday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 
         'Thursday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 'Friday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 'Saturday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"], 'Sunday': ["at 4pm Read the 'The Children of Captain Grant'", 
         "at 8pm Meeting with friend Ivan"]}
day = input(
    'Enter day of week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or number of day: ')
if day.isdigit():
    number = (int(day) - 1)
    if 0 < number < 8:
        day = day_of_week[number]
if day in day_of_week:
    day = day_of_Week[day_of_week.index(day)]
if day in day_of_Week:
    print('You have', len(diary[day]), 'tasks on', day)
    print(*diary[day], sep='\n')
else:
    print('You make mistake')
    

