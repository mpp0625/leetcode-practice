def lengthOfLongestSubstring1(s: str) -> int:
    length = 0
    curr_str = ""

    for c in s:
        if c not in curr_str:
            curr_str += c
            continue
        
        length = max(length, len(curr_str))

        index = curr_str.index(c)
        curr_str = curr_str[index + 1: ]
        curr_str += c

    return length


def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    occ = set()

    rk, ans = 0, 0

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])

        while rk < n and s[rk] not in occ:
            occ.add(s[rk])
            rk += 1

        ans = max(ans, rk - i)

    return ans


s = "abcabcbb"
# s = " "
print(lengthOfLongestSubstring2(s))


"""
lengthOfLongestSubstring1 字符串切片：
    ...
    时间复杂度：
        index()、in、字符串切片的时间复杂度为 O(m)，m 是 curr_str 的长度；
        所以总的时间复杂度： O(m * n)；空间复杂度： O(m)；

lengthOfLongestSubstring2 滑动窗口 + set:

"""