input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 지정 변수 방법
    max_num = array[0]      # 대입 연산 1번 실행
    for num in array:       # array 의 길이만큼 아래 연산이 실행
        if num > max_num:   # 비교 연산 1번 실행
            max_num = num   # 대입 연산 1번 실행

    return max_num

# array의길이 * (비교연산 1번 + 대입연산 2번)
# 1 + 2 * N = 2N + 1


result = find_max_num(input)
print(result)
