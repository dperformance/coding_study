

# input = "abadabac"
input = "aabbcc"


def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    print(alphabet_occurrence_array)
    print(range(len(alphabet_occurrence_array)))

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"

    # 아래와 같이 풀이도 가능하다.
    # char_count = collections.defaultdict(int)
    #
    # for char in strs:
    #     if char.isalpha():
    #         char_count[char] += 1
    #
    # for k, v in char_count.items():
    #     if v == 1:
    #         return k
    #
    # return "_"



result = find_not_repeating_first_character(input)
print(result)