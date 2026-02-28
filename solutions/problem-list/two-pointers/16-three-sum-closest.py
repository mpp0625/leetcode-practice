from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()

    n = len(nums)
    best = 10 ** 7

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1

        while l < r:
            s = nums[l] + nums[r] + nums[i]

            if s == target:
                return target

            if abs(target - s) < abs(target - best):
                best = s

            if s > target:
                r -= 1

                while l < r and nums[r + 1] == nums[r]:
                    r -= 1

            elif s < target:
                l += 1

                while l < r and nums[l - 1] == nums[l]:
                    l += 1

    return best


nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2

print(threeSumClosest(nums, target))