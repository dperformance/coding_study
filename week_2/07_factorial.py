"""
    3! 은 3 * 2 * 1 = 6,
    4! 는 4 * 3 * 2 * 1 = 4 * 3! = 24

    즉,
    Factorial(n) = n * Factorial(n - 1)
    Factorial(n - 1) = (n - 1) * Factorial(n - 2)
    ....
    Factorial(1) = 1

    n의 값이 5라고 가정하면
    5 * factorial(n - 1)

    5  = (5 * 24 = 120)
    4  = (4 *  6 =  24)
    3  = (3 *  2 =   6)
    2  = (2 *  1 =   2)
    1  =  1

"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))