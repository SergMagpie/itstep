def min_sum_10(nums, start_position=0, best_position=0):
    # print(start_position, nums[start_position:start_position + 10], sum(nums[start_position:start_position + 10]))
    if start_position == len(nums) - 10:
        return best_position
    else:
        if sum(nums[start_position:start_position + 10]) < \
           sum(nums[best_position:best_position + 10]):
            best_position = start_position
        return min_sum_10(nums, start_position + 1, best_position)


if __name__ == "__main__":
    print(min_sum_10(list(range(100))))
    print(min_sum_10(list(range(100, 0, -1))))
    print(min_sum_10(list(range(-50, 50))))
    print(min_sum_10([100, 1, 2, 3, 4, 50, 6, 7, 8, 9, 100, 11, 12, 13, 14,
                      15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                      29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                      43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                      57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                      71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                      85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                      99]))
    print(min_sum_10([
        0, 1, 2, 3, 4, 5, 6, 7, 8, 90, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99
    ]))
