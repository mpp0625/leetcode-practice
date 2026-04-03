from typing import List


def maxProduct1(nums: List[int]) -> int:
    dp_max = [nums[0]]
    dp_min = [nums[0]]

    for i in range(1, len(nums)):
        dp_max.append(max([nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]]))
        dp_min.append(min([nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]]))

    return max(dp_max)


def maxProduct2(nums: List[int]) -> int:
    maxN, minN, ans = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        maxN, minN = \
            max(nums[i], nums[i] * maxN, nums[i] * minN), min(nums[i], nums[i] * maxN, nums[i] * minN)

        ans = max(ans, maxN)

    return ans


nums = [-4,-3,-2]  # [2,3,-2,4]
print(maxProduct2(nums))


"""
maxProduct1 动态规划:
    dp_max[i]: 表示以 nums[i] 结尾的子数组的最大乘积；
    dp_min[i]: 表示以 nums[i] 结尾的子数组的最小乘积；由于乘积可能为负数，所以需要同时维护最大值和最小值；

    状态转移：
        dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]);
        dp_min[i] = min(nums[i], nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]);

    时间复杂度: O(n); 空间复杂度: O(n);


maxProduct2:
    为 maxProduct1 的空间优化版本，使用 maxN 和 minN 代替 dp_max[i - 1] 和 dp_min[i - 1];

    时间复杂度: O(n); 空间复杂度: O(1);

"""