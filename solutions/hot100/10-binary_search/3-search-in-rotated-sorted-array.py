from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1

    while l <= r:
        m = (r- l) // 2 + l

        if nums[m] == target:
            return m

        if nums[0] <= nums[m]:
            if nums[0] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        else:
            if nums[m] < target <= nums[n - 1]:
                l = m + 1
            else:
                r = m - 1

    return -1


nums = [5,1,3]
target = 3

print(search(nums, target))
