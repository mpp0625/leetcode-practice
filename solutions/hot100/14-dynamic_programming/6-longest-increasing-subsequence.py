from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]  # [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))


"""
lengthOfLIS 动态规划:
    dp[i]: 表示的是以 nums[i] 结尾的最长递增子序列的长度；
        每个元素自己就是一个长度为 1 的子序列，所以最初的 dp[i] = 1;
    
    状态转移：对于每个 i, 往前找所有 j < i, 如果 nums[j] < nums[i]，说明 nums[i] 可以接在 nums[j] 后面：
        dp[i] = max(dp[j] + 1), 其中 j 满足 nums[j] < nums[i];
"""