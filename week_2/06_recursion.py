"""
    recursion (재귀)
    - 정의 :어떠한 것을 정의할 때 자신을 참조하는 것을 뜻한다.
    - 사용하는 이유 : 간결하고 효율성 있는 코드를 작성할 수 있다.
"""


def count_down(number):
    if number < 0:
        return
    # print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)
