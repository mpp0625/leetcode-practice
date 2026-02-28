from typing import List


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)

    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_streak = 1
            current_num = num + 1

            while current_num in num_set:
                current_streak += 1
                current_num += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))


"""
set: only duplication, `num - 1 not in num_set` restart counting(not need sort).
"""