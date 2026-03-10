from typing import List


def findAnagrams1(s: str, p: str) -> List[int]:
    s_len, p_len = len(s), len(p)
    
    if s_len < p_len:
        return []

    s_count = [0] * 26
    p_count = [0] * 26

    ans = []

    num_ascii = 97

    for i in range(p_len):
        p_count[ord(p[i]) - num_ascii] += 1
        s_count[ord(s[i]) - num_ascii] += 1

    if s_count == p_count:
        ans.append(0)

    for i in range(s_len - p_len):
        s_count[ord(s[i]) - num_ascii] -= 1
        s_count[ord(s[i + p_len]) - num_ascii] += 1

        if s_count == p_count:
            ans.append(i + 1)

    return ans


def findAnagrams2(s: str, p: str) -> List[int]:
    s_len, p_len = len(s), len(p)
    
    if s_len < p_len:
        return []

    ans = []

    num_ascii = 97
    count = [0] * 26

    for i in range(p_len):
        count[ord(s[i]) - num_ascii] += 1
        count[ord(p[i]) - num_ascii] -= 1

    differ = [c != 0 for c in count].count(True)

    if differ == 0:
        ans.append(0)

    for i in range(s_len - p_len):
        if count[ord(s[i]) - num_ascii] == 1:
            differ -= 1
        elif count[ord(s[i]) - num_ascii] == 0:
            differ += 1

        count[ord(s[i]) - num_ascii] -= 1

        if count[ord(s[i + p_len]) - num_ascii] == -1:
            differ -= 1
        elif count[ord(s[i + p_len]) - num_ascii] == 0:
            differ += 1

        count[ord(s[i + p_len]) - num_ascii] += 1

        if differ == 0:
            ans.append(i + 1)

    return ans


s = "abab"
p = "ab"

print(findAnagrams2(s, p))


"""
findAnagrams1 滑动窗口 + 计数数组：
    时间复杂度： O(m + (n - m) x Σ)，其中 n 是字符串 s 的长度，Σ=26 为所有可能的字符数；
        Σ：每次判断滑动窗口中每种字母的数量是否与字符串 p 中每种字母的数量相同；
    空间复杂度： O(Σ)，因为计数数组的大小是固定的。

findAnagrams2 滑动窗口 + 计数数组 + differ 变量：
    count: 记录的是窗口中字母出现次数与 p 中字母出现次数的差值;
    differ: 记录 count 中不为 0 的元素的数量；

    每次滑动窗口变化时，真正影响 differ 变化的是上一个窗口的第一个字符和新窗口的最后一个字符；
    上一个窗口的第一个字符：
        如果它在 count 中的为 1, 那么 differ `减` 1;
            等于 1 说明滑窗中该字符只比 p 中该字符数量多了一个，此时滑过它数量刚好相等;
            大于 1 说明就算滑过这个字符，滑窗中该字符数量与 p 中的仍然不同，只能在 count 中`减1`;
        如果它在 count 中的为 0, 那么 differ `加` 1;
        `count` 中这个字符的数量 `减` 1;

    新窗口的最后一个字符：
        如果它在 count 中的为 -1, 说明只要加上当前的这个字符就与 p 中的相同，那么 differ `减` 1;
        如果它在 count 中的为 0, 说明只要加上当前的这个字符就比 p 中的多了一个，那么 differ `加` 1;
        `count` 中这个字符的数量 `加` 1;

    时间复杂度：O(m + Σ + (n - m))；空间复杂度： O(Σ)
"""