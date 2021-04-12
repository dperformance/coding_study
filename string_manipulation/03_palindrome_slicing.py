import re

strs1 = "A man, a plan, a canal: Panama"
strs2 = "race a car"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        print(s)

        return s == s[::-1]  # 슬라이싱


if __name__ == '__main__':
    s = Solution()

    result = s.isPalindrome(strs1)
    print(result)

    result = s.isPalindrome(strs2)
    print(result)