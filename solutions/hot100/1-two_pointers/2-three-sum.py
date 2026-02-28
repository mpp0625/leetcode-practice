from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []

    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        l, r = i + 1, n - 1

        while l < r:
            t = -(num)
            s = nums[l] + nums[r]

            if  s == t:
                ans.append([num, nums[l], nums[r]])

                l += 1
                r -= 1

                # deduplication
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif s < t:
                l += 1
            else:
                r -= 1

    return ans


nums = [0,0,0,0]
print(threeSum(nums))


"""
先排序，根据和的大小确定指针的移动方向，不排序将无法确定指针如何移动；
注意：一定避免使用双循环，尽量所有算法都是用指针来完成，包括去重（使用指针，而不是使用数组判断是否重复等）；

如何移动指针：
    t: 左右指针求和的目标值； s: 左右指针求和的真实值；
    当 s = t 时，左右指针同时移动；此时需要注意，遇到移动指针前后如果值相同需要跳过避免重复；
    当 s < t 时，说明需要更大的值求和，所以移动左指针；
    当 s > t 时，说明需要更小的值求和，所以移动右指针；
"""