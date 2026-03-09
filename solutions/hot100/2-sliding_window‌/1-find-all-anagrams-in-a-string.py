from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
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


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))