from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def bound(lower):
        n = len(nums)

        l, r = 0, n - 1
        ans = n

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] > target or (lower and nums[mid] >= target):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1

        return ans

    start = bound(True)
    end = bound(False) - 1

    if (start <= end and end < len(nums) and nums[start] == target and nums[end] == target):
        return [start, end]

    return [-1, -1]


nums = [5,7,7,8,8,10]
target = 6

print(searchRange(nums, target))


"""
非递减：序列中的每一个元素都大于或等于它前面的元素；

searchRange 二分查找：
    分两次分别查找开始和结束位置，均使用二分查找；
    时间复杂度: O(logn); 空间复杂度: O(1);
"""