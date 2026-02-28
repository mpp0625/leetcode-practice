from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1

    max_area = 0

    while left < right:
        area = min(height[right], height[left]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))


"""
两层循环，它的时间复杂度是O(n²)，当 `height` 为 10000 时，大约需要执行 1亿次 操作。

如何移动指针：
    相同情况下两边距离越远越好
    区域受限于较短边，移动短边的指针
"""