from typing import List


def maxSubArray1(nums: List[int]) -> int:
    max_sum = cur_sum = nums[0]

    for i in range(1, len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray1(nums))


"""
maxSubArray1 动态规划：
    dp[i] 表示：以 nums[i] 结尾的最大子数组和;
    状态转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i])；要么从 nums[i] 开始，要和延续之前的子数组 + nums[i]

    时间复杂度: O(n); 空间复杂度: O(1)
"""