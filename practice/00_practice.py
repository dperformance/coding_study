import collections
import re
import time
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]


def test(strs: List[str]) -> List[str]:
    # 1. sorted() 사용하여 List 형태로 return 받는다.

    # 2. 정렬된 List 값을 딕셔너리 key 값으로 사용하기 위해 join() 함수를 사용한다.
    #   - defaultdict(list) 사용
    anagrams = collections.defaultdict(list)

    print(sorted(strs))
    for word in strs:
        print(''.join(sorted(word)))
        anagrams[''.join(sorted(word))].append(word)

    print(anagrams)
    print(anagrams.values())

    print()




start = time.time()

print(test(strs))

print("time :", time.time() - start)
