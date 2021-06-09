"""
    * 이진탐색은 무작위로 정렬되어 있는 배열에서는 사용할 수 없다.
    * 오름차순으로 일정하게 정렬되어 있는 데이터일 때만 사용할 수 있다.

- Sequential Search (순차탐색 시간 복잡도)
    target = 15

    for num in array:
        if num == target:
            return True
    return False

    순차적으로 정렬된 배열에서 찾게 된다면 for 문은 총 15번 돌게 된다.
    target = 100 이라면 for 문은 총 100번을 검색해야 하기 때문에
    최악의 경우는 O(n)이 걸린다.

- Binary Search (이진 탐색 시간 복잡도)
    총 숫자가 1 ~ N 까지 있다고 한다면
    1번 탐색하면 반절이 줄어드니 N/2 개가 남는다.
    2번 탐색하면 반절이 줄어드니 N/4 = N/2^2 개가 남는다.
    3번 탐색하면 반절이 줄어드니 N/8 = N/2^3 개가 남는다.
    ....
    k번 탐색하면 반절이 줄어드니 N/2^k 개가 남는다.
    이 때, 이진탐색을 열심히 시도해서 딱 1개만 남았다고 가정을 해보겠습니다.
    이걸 수식으로 표현하면, N/2^k = 1 입니다.
    즉, k = \log_2{N}  횟수를 시도하면 정답을 찾을 수 있습니다!

    결론적으로 이분탐색을 위해서는 시간 복잡도가 O(logN)  만큼 걸린다.
    라고 말할 수 있습니다.

    Q. 여기서 왜 log_2N  이 아니라 logN 인가요?
    A. 상수는 무시해도 되기 때문에 표기하기 쉽도록 logN 으로 부르기로 약속했습니다!

"""


finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def binary_search(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_center = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_center] == target:
            return True
        elif array[current_center] > target:
            current_max = array[current_center] - 1
        else:
            current_min = current_center + 1
        current_center = (current_min + current_max) // 2

    return False


result = binary_search(finding_target, finding_numbers)
print(result)
