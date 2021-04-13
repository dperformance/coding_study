from typing import List

""""
Reorder Log Files
    1. 로그의 가장 앞 부분은 식별자다. (dig1, let1, dig2, let2, let3)
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
    4. 숫자 로그는 입력 순서대로 한다.
"""

"""
Keyword
    1. .split()   - ['dig1 8 1 5 1'] -> ['dig1', '8', '1', '5', '1']
    2. .isdigit() - 숫자로 변환할 수 있는 문자인지 확인하는 함수.
    3. 숫자는 입력순서대로 출력
    4. 문자는 동일할 경우 식별자 순으로 출력 -> 람다 사용
"""

logs_array = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
test_array = ['2 A', '1 B', '4 C', '1 A']


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():    # 식별자 다음이 숫자여부를 파악할 수 있다면 (숫자)
                digits.append(log)          # digits append
            else:                           # 식별자 다음이 숫자여보를 파악할 수 없다면 (문자)
                letters.append(log)         # letters append

        print("letters :", letters)
        # 문자열[1:]을 키로 하여 정렬하며, 문자열이 동일한 경우 후순위로 시별자 [0]를 지정해 정렬하도록 한다.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        print("ttt :", letters)

        def func(x):
            print("test : ", x.split()[1], x.split()[0])
            return x.split()[1], x.split()[0]

        letters.sort(key=func)

        return letters + digits


s = Solution()
result = s.reorderLogFiles(logs_array)
print(result)
