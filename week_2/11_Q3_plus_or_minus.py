"""
    - 더하거나 빼거나
    Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3

        사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

    :keyword
        [2, 3, 1]
        1. +2 +3 +1 =  6  +++
        2. +2 +3 -1 =  4  ++-
        3. +2 -3 +1 =  0  +-+
        4. +2 -3 -1 = -2  +--
        5. -2 +3 +1 =  2  -++
        6. -2 +3 -1 =  0  -+-
        7. -2 -3 +1 = -4  --+
        8. -2 -3 -1 = -6  ---

        앞에 있는 2개를 고정시키면 뒤에 있는 것이 + 혹은 -로 바꾸면 두가지 경우의 수가 추가적으로 생긴다.
        즉 마지막에 들어오는 새로운 원소를 뺄지 더할지에 따라 방법이 두 가지가 추가된다.

        * N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
        N - 1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다.

        ex)
        [2, 3]
        1. +2 +3 +1 = +2 +3 +1
                 -1 = +2 +3 -1
        2. +2 -3 +1 = +2 -3 +1
                 -1 = +2 -3 -1
        3. -2 +3 +1 = -2 +3 +1
                 -1 = -2 +3 -1
        4. -2 -3 +1 = -2 -3 +1
                 -1 = -2 -3 -1

"""


numbers = [1, 1, 1, 1, 1]
target_number = 3
# numbers = [2, 3, 1]
# target_number = 0
result = []

# all_ways = result = []
# current_index = 0
# current_sum = 0
# array = [2, 3, 1]

def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array):
        all_ways.append(current_sum)
        return
    print(array, current_index, current_sum, all_ways)
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum + numbers[current_index], all_ways
    ) # (array, 1, 0 + 2, all_ways)
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum - numbers[current_index], all_ways
    ) # (array, 1, 0 - 2, all_ways)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    return 5


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환
print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))
