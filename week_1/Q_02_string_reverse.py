"""
Q.
0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

    input = "0001100"
"""
"""
KeyWord
    이 문자열을 모두 0 혹은 1로 만들기 위해서는 두가지 방법이 있습니다.

    1. 모두 0으로 만드는 방법
    1) 4번째 원소와 5번째 원소를 잡고 뒤집으면? 0000000 이 됩니다.
    
    문자열을 순서대로 탐색하다보면
    뒤집는 시점은 바로 0에서 1로 변할 때 뒤집어야 하는 걸 감지할 수 있습니다!
    
    
    2. 모두 1으로 만드는 방법
    1) 1번째 원소와 3번째 원소를 잡고 뒤집으면? 1111100 이 됩니다. 
    2) 6번째 원소와 7번째 원소를 잡고 뒤집으면? 1111111 이 됩니다.
    
    문자열을 순서대로 탐색하다보면
    뒤집는 시점은 1에서 0으로 변할 때 뒤집어야 하는 걸 감지할 수 있습니다.
    
    즉, 모두 0으로 만드는 방법이 1회이므로 최소 횟수입니다!
"""

# input = "010110"
input = "1110011"
# input = "0001100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_zero = 0
    count_one = 0

    if string[0] == '0':
        count_one = 1
    elif string[0] == '1':
        count_zero = 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_one += 1
            if string[i + 1] == '1':
                count_zero += 1

    return min(count_zero, count_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)