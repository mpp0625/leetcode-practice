from typing import List


def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    hashmap = {}

    for str in strs:
        sorted_str = "".join(sorted(str))
        
        if sorted_str in hashmap:
            hashmap[sorted_str].append(str)
            continue

        hashmap[sorted_str] = [str]

    return list(hashmap.values())


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    from collections import defaultdict

    hashmap = defaultdict(list)

    for str in strs:
        sorted_str = "".join(sorted(str))
        hashmap[sorted_str].append(str)

    return list(hashmap.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams1(strs)


"""
The running time of the two methods is not much different, `strs * 1000000`:
    groupAnagrams1: 2.9213578701019287 seconds
    groupAnagrams2: 2.547487258911133  seconds
"""


