"""
팰린드롬 (Palindrome)
    앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 뜻한다.
    우리말로는 '회문(回文)'이라 부르며, 대표적으로 '소주 만 명만 주소' 가 해당한다.
"""

# isalnum() 영문자, 숫자 여부만 판단하는 함수

# Q :  주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로한다.
strs1 = "A man, a plan, a canal: Panama"
strs2 = "race a car"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                print(strs)

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(strs1)
    print(result)

    result = s.isPalindrome(strs2)
    print(result)
