from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i, num in enumerate(nums):
        delta = target - num

        if delta in hashmap:
            return [hashmap[delta], i]

        hashmap[num] = i

    return []
    

nums = [3,3]
target = 6

print(twoSum(nums, target))