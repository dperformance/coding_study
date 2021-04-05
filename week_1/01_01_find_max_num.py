input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이중 반복문 구조
    # for num in array:               # array 의 길이만큼 아래 연산이 실행
    #     for compare_num in array:   # array 의 길이만큼 아래 연산이 실행
    #         if num < compare_num:   # 비교 연산 1번 실행
    #             break
    #     else:
    #         return num
    # N * N = N2
    # 6 * 6 = 36
    # array(입력값) -> 입력값은 함수에서 크기가 변경될 수 있는 값이다.
    # N의 크기에 따른 시간의 상관관계를 시간복잡도라 하기 때문에 수식으로 표현해야 한다(N * N = N2)
    # 따라서 이중 반복문 구조는 N2만큼의 시간이 걸렸겠구나!

    # 이 부분을 채워보세요!
    for num in array:
        print("num : ", num)
        for compare_num in array:
            print("compare_num : ", compare_num)
            if num < compare_num:
                break
        else:
            print("end : ", num)
            return num


result = find_max_num(input)
print(result)
