from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    n = len(nums)
    ans = []

    for i in range(n - 3):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        for j in range(i + 1, n - 2, 1):
            if j > i+ 1 and nums[j - 1] == nums[j]:
                continue

            l, r = j + 1, n - 1

            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]

                if s == target:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1

                else:
                    r -= 1

    return ans


nums = [-2,-1,-1,1,1,2,2]
target = 0

print(fourSum(nums, target))