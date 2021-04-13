from typing import List
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
output = "ball"

"""
Most Common Word (가장 흔한 단어)
    금지된 단어 "ball"을 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 
    구두점(마침표, 쉼표 등) 또한 무시한다.
"""

"""
Keyword
    1. 입력값에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재.
    2. 데이터 클렌징(Data Cleansing)이라 부르는 입력값에 대한 전처리(Preprocessing) 작업 필요
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 리스트 컴프리헨션
        # \w는 단어 문자(Word Character)를 의미
        # ^은 not을 의미
        # 따라서 아래 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환(Substitute)하는 역할
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()                # 소문자로 잘라내기
                 if word not in banned]     # banned["hit"] 단어는 제외한 목록을 저장하라.
        print("리스트 컴프리헨션 완료 :", words)

        counts_1 = collections.defaultdict(int)
        for word in words:
            counts_1[word] += 1
        print("defaultdict  :", counts_1)

        counts = collections.Counter(words)
        print("Counter      :", counts)
        print("가장흔한 단어  :", counts.most_common(1)[0][0])
        print("가장흔한 단어수 :", counts.most_common(1)[0][1])

        return counts.most_common(1)[0][0]


s = Solution()
result = s.mostCommonWord(paragraph, banned)
print("result       :", result)
