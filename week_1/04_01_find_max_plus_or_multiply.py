"""
 Todo
 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
 숫자 사이에 '*' 또는 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.
 단, '+' 보다 '*'를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
"""

"""
Result
 3 * 0 = 0  /  3 * 1 = 3
 3 + 0 = 3  /  3 + 1 = 4
 무조건 곱하기만 해서는 최대의 값이 나오지 않는다.
 1과 같거나 적을때는 더하기를 해야 한다.
"""

# 시간복잡도
# 반복문이 1개 들어갔기 때문에 O(N)이다.


input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiple_sum = 0;
    for number in array:
        if number <= 1 or multiple_sum <= 1:
            multiple_sum += number
            print("number <= 1 : ", number, multiple_sum)
        else:
            multiple_sum *= number
            print("number >= 1 : ", number, multiple_sum)
    return multiple_sum


result = find_max_plus_or_multiply(input)
print(result)