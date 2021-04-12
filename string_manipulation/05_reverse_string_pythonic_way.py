from typing import List


strs1 = ["h", "e", "l", "l", "o"]
strs2 = ["H", "a", "n", "n", "a", "h"]


# Pythonic Way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        print(s)


s = Solution()
s.reverseString(strs1)
s.reverseString(strs2)

