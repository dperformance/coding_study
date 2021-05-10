import collections, re
from typing import Deque


strs1 = "A man, a plan, a canal: Panama"
strs2 = "race a car"


class Solution:
    # 1. 문자열과 숫자만 소문자로 변환하라.

    strs2 = []

    # List 방법
    def isPalindromeList(self, strings: str) -> bool:
        strs = []
        for char in strings:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True


    # Deque 방법
    def isPalidromeDeque(self, strings: str) -> bool:
        strs: Deque = collections.deque()
        for char in strings:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


    # 정규표현식 & slicing 방법
    def isPalindromeSlicing(self, strings: str) -> bool:
        strs = strings.lower()
        strs = re.sub('[^a-z0-9]', '', strs)
        print("ttt :", strs)
        if strs != strs[::-1]:
            return False
        return True


s = Solution()
print(s.isPalindromeList(strs1))
print(s.isPalindromeList(strs2))
