from typing import List


def rotate1(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    dummy = [0] * n

    for i in range(n):
        dummy[(i + k) % n] = nums[i]

    for i in range(n):
        nums[i] = dummy[i]

    print(nums)


def rotate2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """



nums = [-1,-100,3,99]
k = 2

print(rotate1(nums, k))


"""
rotate1 使用额外数组:
    时间复杂度: O(n)
"""