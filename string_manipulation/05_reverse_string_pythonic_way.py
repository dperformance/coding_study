from typing import List


strs1 = ["h", "e", "l", "l", "o"]
strs2 = ["H", "a", "n", "n", "a", "h"]

# reverse()함수는 List 만 지원한다.
# slicing 또한 문자열, 문자 배열 둘다 지원한다.


# Pythonic Way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        print(s[:])
        print(s[:: -1])
        s.reverse()
        print(s)


s = Solution()
s.reverseString(strs1)
s.reverseString(strs2)

