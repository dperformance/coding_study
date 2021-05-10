from collections import generator
from typing import List

input: List[int] = [3, 5, 7, 1, 2, 4]


def findMaxNum(input: List[int]) -> int:
    a: List[int] = []
    for n in range(1, 10 + 1):
        print(n)

    for i in input:
        for j in input:
            if i < j:
                print(i, j)
                break
        else:
            return i


def find_max_num1(input: List[int]) -> int:
    max_num = input[0]
    for i in input:
        if max_num < i:
            max_num = i
    return max_num


def get_natual_number() -> generator:
    n: int = 0
    while range(0, 100):
        n += 1
        yield n


# print(findMaxNum(input))
#
# print(find_max_num1(input))

print(type(get_natual_number()))
