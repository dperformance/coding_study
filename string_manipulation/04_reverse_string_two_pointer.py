from typing import List


strs1 = ["h", "e", "l", "l", "o"]
strs2 = ["H", "a", "n", "n", "a", "h"]


"""
 Reverse String (Two Pointer)
       문자 배열을 뒤집기
       left, right 변수를 이용하여 s 내부를 스왑하는 형식으로 진행된다.
"""
# Q : 문자열을 뒤집는 함수를 작성하라, 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        # 0 / 4
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = Solution()

    s.reverseString(strs1)
    s.reverseString(strs2)
