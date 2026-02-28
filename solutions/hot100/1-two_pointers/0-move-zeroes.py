from typing import List


def moveZeroes1(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    left, right = 0, len(nums) - 1

    while left < right:
        num = nums[left]

        if num == 0:
            nums.pop(left)
            nums.append(num)

            right -= 1

        else:
            left += 1

    return nums


def moveZeroes2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    left, right = 0, 0

    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        right += 1

    return nums


nums = [0,1,0,3,12]
print(moveZeroes2(nums))


"""
使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。

注意到以下性质：
    1. 左指针左边均为非零数；
    2. 右指针左边直到左指针处均为零。

因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。
"""