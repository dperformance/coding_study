from typing import List

"""
Two Sum
    
"""
# Q : 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [2, 7, 11, 15]
# nums = [2, 11, 15, 7]
target = 9
output = [0, 1]


class Solution:
    # 브루트 포스 O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색 O(n)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):        # 0번 즉 2값을 n으로 받아 온다.
            complement = target - n         # 9 - 2 = 7(complement)
            if complement in nums[i + 1:]:  # 7이라는 값이 1번 index 부터 있는지 검사한다.
                #       2 = 0(index), nums[1:] [11,15,7] .index(7) = 2 (0 + 1) = 3
                #            0      , 3
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    # 첫 번째 수를 뺀 결과 키 조회
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 딕셔너리(map) 변수 선언
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            #    9 - 2 = 7                  0 !=             9   -  2
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]

    # 조회 구조 개선
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                print("ttt : ", target - num, num, i)
                return [nums_map[target - num], i]
            nums_map[num] = i
            print("nums_map :", nums_map)

    # 투 포인터 이용
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while not left == right:
            # 합이 타켓보다 작으면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타켓보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right


s = Solution()
result = s.twoSum(nums, target)
print("twoSum   :", result)

result = s.twoSum1(nums, target)
print("twoSum1  :", result)

result = s.twoSum2(nums, target)
print("twoSum2  :", result)

result = s.twoSum3(nums, target)
print("twoSum3  :", result)

result = s.twoSum4(nums, target)
print("twoSum4  :", result)
