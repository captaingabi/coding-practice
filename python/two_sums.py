#!/bin/python3

def twoSum(nums: list[int], target: int) -> list[int]:
    i: int = 0
    while i < len(nums) - 1:
        j: int = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
