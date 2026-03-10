from typing import List
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    sum = [0] * (n + 1)

    for i, num in enumerate(nums):
        sum[i + 1] = sum[i] + num

    ans = 0
    d = defaultdict(int)

    for s in sum:
        ans += d[s - k]
        d[s] += 1

    return ans


def subarraySum2(nums, k):
    ans = 0
    sum = 0

    d = {0: 1}

    for num in nums:
        sum += num

        if sum - k in d:
            ans += d[sum - k]

        d[sum] = d.get(sum, 0) + 1

    return ans


nums = [1,-1,0]
k = 0

print(subarraySum2(nums, k))


"""
sum:
    sum[0] = 0
    sum[1] = nums[0]
    sum[2] = nums[0] + nums[1]
    ......

    子数组: nums[i ... j], 其和为 sum[j + 1] - sum[i]
        sum[i]     = nums[0] + ... + nums[i - 1]
        sum[j + 1] = nums[0] + ... + nums[i - 1] + nums[i] + ... + nums[j]

        nums[i ... j] = sum[j + 1] - sum[i]  ->
        sum[j + 1] - sum[i] = k (子数组的和)  -> 
        sum[i] = sum[j - 1] - k

        假设现在遍历到了某个前缀和: s = sum[j+1] ->
        想要找到一个之前的位置 i: sum[i] = s - k ->
        如果找到了说明 s - (s - k) = k (sum[j+1](s) - sum[i](s - k) = k), 存在子数组和为 k

    d: {前缀和: count}, 前缀和是由连续的子数组得到的；
    本质上：当前前缀和 - k 在 d 中的次数；
"""