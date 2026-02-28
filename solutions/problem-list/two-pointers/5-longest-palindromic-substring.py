def longestPalindrome1(s: str) -> str:
    def validPalindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    n = len(s)

    if n <= 1:
        return s

    begin, max_len = 0, 0

    for i in range(n):
        for j in range(i + 1, n, 1):
            if j - i + 1 > max_len and validPalindrome(i, j):
                begin = i
                max_len = j - i + 1

    return s[begin: begin + max_len]


def longestPalindrome2(s: str) -> str:
    def expandAroundCenter(l, r):
        while l > -1 and r < n and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1

    n = len(s)

    if n <= 1:
        return s

    begin, max_len = 0, 0

    for i in range(n - 1):
        len1 = expandAroundCenter(i, i)  # odd
        len2 = expandAroundCenter(i, i + 1)  # even

        cur_len = max(len1, len2)

        if cur_len > max_len:
            max_len = cur_len
            begin = i - (cur_len - 1) // 2

    return s[begin: begin + max_len]


def longestPalindrome3(s: str) -> str:
    n = len(s)

    begin, max_len = 0, 0

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for j in range(n):
        for i in range(n):
            if i > j:
                break

            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

                if j - i > max_len:
                    max_len = j - i
                    begin = i

    return s[begin: begin + max_len + 1]


s = "aaaa"
print(longestPalindrome3(s))


"""
longestPalindrome1: 暴力法，时间复杂度 O(n³)，它是将当前索引当作为左指针，将字符串末位当成初始右指针，过程中一种指针的方式复杂；

longestPalindrome2: 中心扩展法，将当前索引位置作为中心像两侧扩展，时间复杂度 O(n²)
    如何变化指针：
        当 s[l] == s[r] 时，同时变化左右指针，索引超出范围后停止；
        需要注意的数，需要同时考虑奇数、偶数两种变化，比如 `cbbc`、`bab`

longestPalindrome3: 动态规划法 - 空间换时间，时间复杂度 O(n²)
    一个回文去掉两头后依然是回文，当一个子串的两头：
        如果不相等就不是回文；
        如果相等则需要看剩下的子串是不是回文；

    定义状态: dp[i][j] 表示子串 s[i: j + 1] 是否是回文 (i ~ j 的子串)
    状态转移方程: dp[i][j] = s[i] == s[j] & dp[i + 1][j - 1]，对角线的 dp[i][i] = True
    边界条件: j - 1 - (i + 1) >= 1  -> j - i >= 3 才需要判断是否为回文子串，如果 j - i < 3 可以直接判定为 True
    判断条件: s[i] == s[j] & (j - i < 3 or dp[i + 1][j - 1])

    生成二维表格数据：
        横向为 `右边界`，纵向为 `左边界`；
        由于添加 i <= j 限制，所以 dp 只需要填写对角线上的部分；
        由于当前 dp[i][j] 依赖于二维表格中其左下方的值，所以先按照列遍历；


时间对比结果：中心扩散法 > 动态规划 > 暴力法
"""