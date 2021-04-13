from typing import List

"""
Two Sum
    
"""
# Q : 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [2, 7, 11, 15]
target = 9
output = [0, 1]


class Solution:
    # 브루트 포스 O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색 O(n)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        test_digit = 1
        test_digit = 2
        test_digit = 3
        test_digit = 4
        print("test_digit :", test_digit)

        print(enumerate(nums))
        for i, n in enumerate(nums):
            print("enumerate 에서 넘어온 값 : ", i, n)

            complement = target - n
            print("complement :", complement)
            print("test_code  :", nums[i + 1:])

            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    #
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]
        

s = Solution()
result = s.twoSum(nums, target)
print(result)

result = s.twoSum1(nums, target)
print(result)

result = s.twoSum2(nums, target)
print(result)