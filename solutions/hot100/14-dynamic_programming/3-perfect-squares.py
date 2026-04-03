def numSquares(n: int) -> int:
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        minn = int(1e10)

        j = 1
        while j ** 2 <= i:
            minn = min(minn, dp[i - j ** 2] + 1)
            j += 1

        dp[i] = minn

    return dp[-1]

n = 12
print(numSquares(n))


"""
numSquares 动态规划：
    定义状态: dp[i] 表示数字 i 的完全平方数的最少数量;
    状态转移方程: dp[i] = min(dp[i - j ** 2] + 1) for j in range(1, i) if i >= j ** 2;

    时间复杂度: O(n * sqrt(n)); 空间复杂度: O(n);
"""