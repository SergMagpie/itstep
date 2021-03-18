def to_do_list():
    '''
    Key features:
    - The user can add a new task
    - the user can edit the task
    - the user can delete the task
    - the user can mark the task as completed
    - the user can view the list of completed and
    unfulfilled tasks and deduce to understand which of
    tasks has what status.
    '''
    def write_list(task_list: list, filename='list_whith_tasks.txt', sep='|'):
        """
        Function for write list.
        """
        with open(filename, "w") as f:
            for i in task_list:
                f.write(sep.join([x for x in i]) + sep + '\n')

    def read_dict(filename='list_whith_tasks.txt', sep='|') -> list:
        """
        Function for read list.
        File integrity check not implemented, if necessary,
        I can add a checksum. But this is not all today.
        """
        try:
            with open(filename, "r") as f:
                task_list = []
                for line in f:
                    values = line.split(sep)
                    task_list.append(values[:2])
        except:
            key = input('The file is damaged. Create a new file? y/n ')
            task_list = [[]]
            if key == 'y':
                write_list(task_list)
        return task_list

    def add_a_new_task():
        task = input('\nEnter new task: ')
        task_list.append(["unfulfilled", task])
        print('Task added')

    def edit_the_task():
        num = input('Enter a number of task for editng ')
        if num.isdigit():
            num = int(num) - 1
            if 0 <= num < len(task_list):
                print('You are editing task: {}'.format(task_list[num][1]))
                task_list[num][1] = input('Enter an editing task: ')
                print('Task edited')
            else:
                print('You made mistake')
        else:
            print('You made mistake')

    def delete_the_task():
        num = input('\nEnter a number of task for deleting ')
        if num.isdigit():
            num = int(num) - 1
            if 0 <= num < len(task_list):
                key = input(
                    'Are you sure deleted task: {} ? y/n'.format(task_list[num][1]))
                if key == 'y':
                    del task_list[num]
                    print('Task deleted')
            else:
                print('You made mistake')
        else:
            print('You made mistake')

    def mark_the_task_as_completed():
        num = input('\nEnter a number of task for mark ')
        if num.isdigit():
            num = int(num) - 1
            if 0 <= num < len(task_list):
                if task_list[num][0] == "unfulfilled":
                    task_list[num][0] = "completed"
                else:
                    task_list[num][0] = "unfulfilled"
                print('Task marked')
            else:
                print('You made mistake')
        else:
            print('You made mistake')

    def view_the_list():
        print('\nYour tasks:')
        for n, [i, j] in enumerate(task_list):
            print(n + 1, i, j)

    def good_by():
        print('Good by! See you later!')
        write_list(task_list)

    task_list = read_dict()
    print(task_list)

    box = {
        "a": add_a_new_task,
        "e": edit_the_task,
        "d": delete_the_task,
        "m": mark_the_task_as_completed,
        "v": view_the_list,
        "exit": good_by,
    }

    key = ''
    while key != 'exit':
        print("\nHello I'm your To Do list")
        print("Enter A for add a new task")
        print("Enter E for edit the task")
        print("Enter D for delete the task")
        print("Enter M for mark/unmark the task as completed")
        print("Enter F for view the list")
        print("Enter EXIT for exit")
        key = input("Make your choice: ").lower()
        if key in box:
            box[key]()
        else:
            print('You made mistake')


if __name__ == "__main__":
    import os
    # Actualised a directory with a script.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    to_do_list()
