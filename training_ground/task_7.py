def if_happy(num):
    string_nums = [int(i) for i in list(str(num))]
    if sum(string_nums[:3]) == sum(string_nums[3:]):
        return True
    else:
        return False


print(if_happy(123420))
print(if_happy(723422))
