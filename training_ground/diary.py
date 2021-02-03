day_of_week = ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday']
diary = {'Monday': ["at 4pm Read the 'Middlemarch'",
                    "at 8pm Meeting with friend Ivan"],
         'Tuesday': ["at 4pm Read the 'To the Lighthouse'",
                     "at 8pm Meeting with friend Piter"],
         'Wednesday': ["at 4pm Read the 'Mrs. Dalloway'",
                       "at 8pm Meeting with friend Sara"],
         'Thursday': ["at 4pm Read the 'Great Expectations'",
                      "at 8pm Meeting with friend Lora"],
         'Friday': ["at 4pm Read the 'Jane Eyre'",
                    "at 8pm Meeting with friend Nicolas"],
         'Saturday': ["at 4pm Read the 'Bleak House'",
                      "at 8pm Meeting with friend Gorge"],
         'Sunday': ["at 4pm Read the 'The Children of Captain Grant'",
                    "at 8pm Meeting with friend Antonina"]}
day = input('''Enter day of week: Monday, Tuesday, Wednesday, Thursday,\
 Friday, Saturday, Sunday or number of day: ''')
if day.isdigit():
    number = (int(day) - 1)
    if 0 <= number < 7:
        day = day_of_week[number]
else:
    day = day.capitalize()
if day in day_of_week:
    print('You have', len(diary[day]), 'tasks on', day)
    print(*diary[day], sep='\n')
else:
    print('You make mistake')
