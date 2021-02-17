print('Hello, you are greeted by the exercise machine!')
print("Let's do exercises!")
print('And, once, and, once, and once, two three!')
num_approach = 1
list_approach = []
while True:
    number_of_repetitions = input(f"Enter the number of repetitions in \
approach № {num_approach} or 'stop' to stop: ")
    if number_of_repetitions == 'stop':
        break
    elif number_of_repetitions.isdecimal():
        list_approach += [int(number_of_repetitions)]
        num_approach += 1
        print('This is great!')
    else:
        print('You were wrong, come together, be more careful!')
print('You a superman!')
print(f'You have done {len(list_approach)} approaches!')
print(f'The total number of repetitions was {sum(list_approach)}!')
print(f'The maximum number of repetitions was \
{(max(list_approach) if list_approach else 0)}!')
print(f'The minimum number of repetitions was \
{(min(list_approach) if list_approach else 0)}!')
print(f'The average number of repetitions was \
{(sum(list_approach) / len(list_approach) if list_approach else 0)}!')
print('Till next time!')
