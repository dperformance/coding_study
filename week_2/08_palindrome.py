input = "abcba"


def is_palindrome(string: str) -> bool:
    if string != string[::-1]:
        return False
    return True


def is_palindrome_1(string: str) -> bool:
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True


def is_palindrome_2(string: str) -> bool:
    # 재귀함수를 이용
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome_2(string[1:-1])


print(is_palindrome(input))
print(is_palindrome_1(input))
print(is_palindrome_2(input))



