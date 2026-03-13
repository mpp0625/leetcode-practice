from typing import List


def findMin(nums: List[int]) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low < high:
        m = (high - low) // 2 + low

        if nums[m] < nums[high]:
            high = m
        else:
            low = m + 1

    return nums[low]


nums = [3,4,5,1,2]
print(findMin(nums))