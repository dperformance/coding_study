str1 = "babad"
str2 = "cbbd"
str3 = "a"
str4 = "ac"


class Solution:
    def longestPaindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            #   left가 0보다 커     right <= 9               0           0
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1       # -1
                right += 1      #  2
                # print(left + 1, right - 1)
            return s[left + 1:right - 1]

        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


s = Solution()
result = s.longestPaindrome(str1)
print(result)
result = s.longestPaindrome(str2)
print(result)
result = s.longestPaindrome(str3)
print(result)
result = s.longestPaindrome(str4)
print(result)

