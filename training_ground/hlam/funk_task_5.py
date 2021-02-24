def sum_range(start_n, end_n):
    if start_n < end_n:
        n = start_n
        sum_n = 0
        while n <= end_n:
            sum_n += n
            n += 1
        return sum_n
    else:
        return None


print(sum_range(1, 4))
