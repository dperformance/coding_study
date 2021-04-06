"""
팰린드롬 (Palindrome)
    앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 뜻한다.
    우리말로는 '회문(回文)'이라 부르며, 대표적으로 '소주 만 명만 주소' 가 해당한다.
"""
# isalnum() 영문자, 숫자 여부만 판단하는 함수


strs1 = "A man, a plan, a canal: Panama"
strs2 = "race a car"


def isPalindrome(array):
    strs = []
    for char in array:
        if char.isalnum():
            strs.append(char.lower())
            print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


result = isPalindrome(strs1)
print(result)

result = isPalindrome(strs2)
print(result)
