from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [int(1e10)] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != int(1e10) else -1


coins = [1, 2, 5]  # [1, 2, 5] [2] [1]
amount = 14

print(coinChange(coins, amount))


"""
状态转移方程：
    f(i) = min(F(i - Cj)) + 1,
        i 是金额, j 的取值范围是 [1, n], n 是硬币的种类数;
        Cj 是第 j 个硬币的面值;
"""