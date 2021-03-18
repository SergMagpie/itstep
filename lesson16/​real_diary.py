def main():
    # I am using the module for the sole purpose of
    # saving the file to the program directory.
    import os
    # Actualised a directory with a script.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    # Create name of file.
    filename = 'diary.txt'
    # The record distributor, made as a prototype, can
    # be replaced by a more appropriate one.
    sep = '|'

    def write_dict(diary_dict, filename=filename, sep=sep):
        """
        Function for write dict.
        """
        with open(filename, "w") as f:
            for i in diary_dict.keys():
                f.write(i + sep + sep.join([str(x)
                                            for x in diary_dict[i]]) + sep + "\n")

    def read_dict(filename=filename, sep=sep):
        """
        Function for read dict.
        File integrity check not implemented, if necessary, 
        I can add a checksum. But this is not all today.
        """
        try:
            with open(filename, "r") as f:
                diary_dict = {}
                for line in f:
                    values = line.split(sep)
                    diary_dict[values[0]] = \
                        [x for x in values[1:len(values) - 1] if x]
        except:
            key = input('The file is damaged. Create a training diary? y/n ')
            if key == 'y':
                diary_dict = {'Monday': ["at 4pm Read the 'Middlemarch'",
                                         "at 8pm Meeting with friend Ivan"],
                              'Tuesday': ["at 4pm Read the 'To the Lighthouse'",
                                          "at 8pm Meeting with friend Piter"],
                              'Wednesday': ["at 4pm Read the 'Mrs. Dalloway'",
                                            "at 8pm Meeting with friend Sara"],
                              'Thursday': ["at 4pm Read the 'Great Expectations'",
                                           "at 8pm Meeting with friend Lora"],
                              'Friday': ["at 4pm Read the 'Jane Eyre'",
                                         "at 8pm Meeting with friend Nicolas",
                                         "at 10pm We have pyjamas party"],
                              'Saturday': ["at 4pm Read the 'Bleak House'",
                                           "at 8pm Meeting with friend Gorge"],
                              'Sunday': ["at 4pm Read the 'The Children of Captain Grant'",
                                         "at 4pm Read the 'The Children of Captain Grant'",
                                         "at 8pm Meeting with friend Antonina"]}
            else:
                diary_dict = {'Monday': [],
                              'Tuesday': [],
                              'Wednesday': [],
                              'Thursday': [],
                              'Friday': [],
                              'Saturday': [],
                              'Sunday': []}

        return diary_dict

    def choose_a_day():
        """
        The function helps to enter the correct day of the week.
        """
        day_of_week = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']
        while True:
            day = input("Enter day of week: Monday, Tuesday, Wednesday,\n" +
                        "Thursday, Friday, Saturday, Sunday or number of day: ")
            if day.isdigit():
                number = (int(day) - 1)
                if 0 <= number < 7:
                    day = day_of_week[number]
            else:
                day = day.capitalize()
            if day in day_of_week:
                return day
            else:
                print('You make mistake')

    def add_task():
        day = choose_a_day()
        task = input('Enter task for {} '.format(day))
        diary[day] += [task]
        print("Task added!")

    def vew_task():
        day = choose_a_day()
        print('You have', len(diary[day]), 'tasks on', day)
        print(*diary[day], sep='\n')

    def delete_task():
        day = choose_a_day()
        print('You have', len(diary[day]), 'tasks on', day)
        if len(diary[day]):
            for n, i in enumerate(diary[day]):
                print(n + 1, i)
            num = input('Enter number of task for delete ')
            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(diary[day]):
                    print('Do you want to delete the task?')
                    print(diary[day][num - 1])
                    if input('Enter y/n ') in ('y', 'Y'):
                        del diary[day][num - 1]
                        print('Task deleted')
                else:
                    print('You made mistake')
            else:
                print('You made mistake')

    def good_by():
        print('Good by! See you later!')
        write_dict(diary)

    box = {'a': add_task,
           'v': vew_task,
           'd': delete_task,
           'exit': good_by,
           }
    diary = read_dict()
    key = ""
    while key != 'exit':
        print("\nHello, I'm your diary!")
        print("Add a task - A\nView tasks - V\nDelete task - D")
        print("Exit for exit")
        key = input("Make your choice: ").lower()
        if key in box:
            box[key]()
        else:
            print('You make mistake')


if __name__ == "__main__":
    main()
