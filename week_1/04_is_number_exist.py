input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for num in array:       # array 의 길이만큼 실행
        if number == num:   # 비교 연산 1번 실행
            return True     # 총 시간 복잡도는 X * 1 = N

    return False

# 입력값이 3이라면 바로 찾을 수 있지만.
# 만약 4가 입력되었다면 모두 돌아야 찾을 수 있다.
# 따라서 입력값의 분포에 따라서 성능이 변화할 수 있다.

# 최악의 성능 -> 빅오표기법 == O(n)
# 최고의 성능 -> 빅오메가 표기법 == 오메가(1)

# 결론은 최악의 경우를 대비하여 알고리즘에서는 거의 모든 알고리즘을 빅오 표기법으로 분석한다.


result = is_number_exist(1, input)
print(result)