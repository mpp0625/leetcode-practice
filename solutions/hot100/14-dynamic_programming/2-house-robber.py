from typing import List


def rob1(nums: List[int]) -> int:
    p, q = 0, 0

    for i in range(len(nums)):
        r = q
        q = max(nums[i] + p, q)
        p = r

    return q


def rob2(nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


nums = [2,1,1,2]  # [1,2,3,1] [2,7,9,3,1] [2,1,1,2]
print(rob1(nums))


"""
rob1 动态规划：
    定义状态：p, q 分别表示前 i - 2 和前 i - 1 个房子能偷窃到的最大金额;
    状态转移方程：r = q; q = max(nums[i] + p, q); p = r;

    时间复杂度: O(n); 空间复杂度: O(1);

rob2 动态规划 - 数组：
    规则：
        偷窃第 k 间房屋，那么就不能偷窃第 k-1 间房屋，偷窃总金额为前 k-2 间房屋的最高总金额与第 k 间房屋的金额之和。
        不偷窃第 k 间房屋，偷窃总金额为前 k-1 间房屋的最高总金额。
        第 k 间房只有偷不偷两个选择，在两个选项中选择偷窃总金额较大的选项，该选项对应的偷窃总金额即为前 k 间房屋能偷窃到的最高总金额。

    用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：
        dp[i]=max(dp[i - 2]+nums[i], dp[i - 1])

    时间复杂度: O(n); 空间复杂度: O(n);
"""