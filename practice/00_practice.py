import collections
import re
import time
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
output = "ball"

"""
    1. 구두점제거 : , ' ' 
    2. 동일한 문장 카운트
    3. 제외될 문장 처리
"""


def test(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
             if word not in banned]

    p = re.compile('[a-z]+')
    print(p)

    # print(words)

    data = """
    park 800905-1049118
    kim  700905-1059119
    doc aswqe-12343
    ttt 1234567886-123434
    abc 123456-1234567
    """

    pat = re.compile("(\d{6})[-]\d{7}")
    print(pat.sub("\g<1>-*******", data))
    print(data)


start = time.time()
print(test(paragraph, banned))

print("time :", time.time() - start)
