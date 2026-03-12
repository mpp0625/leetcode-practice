from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1
    ans = n

    while l <= r:
        m = (r - l) // 2 + l

        if nums[m] >= target:
            r -= 1
            ans = m
        else:
            l += 1

    return ans


nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))


"""
searchInsert 二分查找：
    nums[pos - 1] < target ≤ nums[pos]
"""