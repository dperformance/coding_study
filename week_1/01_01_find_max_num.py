input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이중 반복문 구조
    for num in array:
        print("num : ", num)
        for compare_num in array:
            print("compare_num : ", compare_num)
            if num < compare_num:
                break
        else:
            return num
    # 이 부분을 채워보세요!

    return num


result = find_max_num(input)
print(result)
