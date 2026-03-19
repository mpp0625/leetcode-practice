import math
from typing import List


def maxProfit1(prices: List[int]) -> int:
    maxprofit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            maxprofit = max(maxprofit, prices[j] - prices[i])

    return maxprofit


def maxProfit2(prices: List[int]) -> int:
    minprofit = math.inf
    maxprofit = 0

    for i in range(len(prices)):
        if prices[i] < minprofit:
            minprofit = prices[i]
        else:
            maxprofit = max(maxprofit, int(prices[i] - minprofit))

    return maxprofit


prices = [7,1,5,3,6,4]
print(maxProfit2(prices))


"""
maxProfit1 暴力解法：
    时间复杂度: O(n²); 空间复杂度: O(1);

maxProfit2 一次循环贪心算法：
    记录在当前 i 之前的最低点 minprofit, 如果 i 小于 minprofit, 则更新 minprofit, 否则更新最高点 maxprofit;
    这是一种假设在当前卖出时 i, 买在了最低点；
    时间复杂度: O(n); 空间复杂度: O(1);
"""