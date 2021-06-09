finding_target = 9
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cur_min = 1
    cur_max = len(array) - 1
    cur_target = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if target == cur_target:
            return True
        elif target > cur_target:
            cur_min = cur_target + 1
        else:
            cur_max = cur_target - 1

        print(cur_min, cur_max)
        cur_target = (cur_min + cur_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
