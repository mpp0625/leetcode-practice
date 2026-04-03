from typing import List


def partitionLabels(s: str) -> List[int]:
    last = [0] * 26
    for i, ch in enumerate(s):
        last[ord(ch) - ord("a")] = i

    partition = []
    start, end = 0, 0

    for i, ch in enumerate(s):
        end = max(end, last[ord(ch) - ord("a")])

        if i == end:
            partition.append(end - start + 1)
            start = i + 1

    return partition


s = "eccbbbbdec"
print(partitionLabels(s))


"""
partitionLabels 贪心算法：
    由于每个字母只能出现在一个片段中，也就是同一个字母的第一次出现的下标位置和最后一次出现的下标位置必须出现在同一个片段中；因此遍历字符串，得到每个字母最后一次出现的效标位置；
        遍历字符串，更新 end;
        当 i = end 时，当前片段结束，更新 start;

    时间复杂度: O(n); 空间复杂度: O(1);
"""