from time import time, sleep
from threading import Thread


def print_max_num(*nums):
    max_num = nums[0]
    for i in nums[1:]:
        if i > max_num:
            max_num = i
    print(f'maximum number {max_num}')


def print_min_num(*nums):
    min_num = nums[0]
    for i in nums[1:]:
        if i < min_num:
            min_num = i
    print(f'minimum number {min_num}')


def print_mid_num(*nums):
    count = 0
    total = 0
    for i in nums:
        count += 1
        total += i
    mid_num = total / count
    print(f'average number {mid_num}')


if __name__ == "__main__":
    x1 = time()
    num = ''
    list_of_nums = []
    while num != 'exit':
        num = input("Enter number or exit for exit ")
        if num.isdigit():
            list_of_nums.append(int(num))
            t1 = Thread(target=print_max_num, args=(list_of_nums))
            t2 = Thread(target=print_min_num, args=(list_of_nums))
            t3 = Thread(target=print_mid_num, args=(list_of_nums))

            t1.start()
            t2.start()
            t3.start()


            print(*list_of_nums)
        elif num == 'exit':
            print('Goodbye!')
        else:
            print("You made a mistake")
