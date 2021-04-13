from typing import List
import collections

"""
Anagrams
    언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
    eat -> tea, ate
"""

"""
Keyword
    
"""


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        print(strs)
        print("sorted()정렬 :", sorted(strs))
        anagrams = collections.defaultdict(list)
        print(anagrams)

        # 정렬하여 딕셔너리에 추가
        for word in strs:
            print("test :", sorted(word), word, ''.join(sorted(word)))
            anagrams[''.join(sorted(word))].append(word)
        print(anagrams)
        anagrams[''.join(sorted('dyson'))].append("테스트다")
        print(anagrams)
        print(anagrams.values())
        print(anagrams.keys())

        return anagrams.values()


s = Solution()
result = s.groupAnagrams(strs)
print("zz :", result)
