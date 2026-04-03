from typing import List


def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    n = sum(nums) // 2

    dp = [0] * (n + 1)
    dp[0] = 1

    for num in nums:
        for i in range(n, num - 1, -1):
           dp[i] = dp[i] or dp[i - num]

    return bool(dp[n])


nums = [3,3,6,8,16,16,16,18,20]  # [2,2,1,1] [3,3,3,4,5] [1,5,11,5] [3,3,6,8,16,16,16,18,20]
print(canPartition(nums))


"""
两个子集和相等，说明每个子集和 = 总和 / 2;

canPartition:
    dp[i]: 表示能否凑出和为 i; i: 0 ~ sum // 2;
           如果想凑出 i, 要么不选当前数 num, 要么选当前数 num, 如果选了当前数 num, 那么之前就要能凑出 i - num;

    dp[i] = dp[i] or dp[i - num];
"""