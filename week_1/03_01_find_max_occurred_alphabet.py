input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array:     # alphabet_array 의 길이(26)만큼 아래 연산이 실행
        occurrence = 0                  # 대입 연산 1번 실행
        for char in string:             # string 의 길이()만큼 아래 연산이 실행
            if char == alphabet:        # 비교 연산 1번 실행
                occurrence += 1         # 대입 연산 1번 실행

        if occurrence > max_occurrence: # 비교 연산 1번 실행
            max_occurrence = occurrence # 대입 연산 1번 실행
            max_alphabet = alphabet     # 대입 연산 1번 실행

    return max_alphabet

    # 대입 연산 4번 실행
    # 비교 연산 2번 실행

result = find_max_occurred_alphabet(input)
print(result)