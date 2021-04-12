import collections
from typing import Deque

strs1 = "A man, a plan, a canal: Panama"
strs2 = "race a car"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():                  # 문자열, 숫자 check
                strs.append(char.lower())       # 소문자로 append

        print(len(strs))
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(strs1)
    print(result)

    result = s.isPalindrome(strs2)
    print(result)



