from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda i: i[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[4,7],[1,4]]
print(merge(intervals))


"""
merge: 排序
    时间复杂度: O(nlog(n)); 空间复杂度: O(m)
"""