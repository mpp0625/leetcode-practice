from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [0] * (len(s) + 1)

    dp[0] = 1

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in wordDict:
                dp[i] = 1
                break

    return bool(dp[-1])


s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

print(wordBreak(s, wordDict))


"""
wordBreak 动态规划：
    dp[i]: 表示字符串 s 的前 i 个字符组成的子串 s[0: i] 是否能被 wordDict 中的单词拼接而成。
    dp[0] = 1: 空字符串可以被拼接而成。

    状态转移：对于每个位置 i, 枚举 j 从 0 到 i-1, 如果 dp[j] 为真且 s[j: i] 在 wordDict 中，则 dp[i] 也为真。
"""