from typing import List


def canJump1(nums: List[int]) -> bool:
    reach = 0

    for i in range(len(nums)):
        if i > reach:
            return False
        
        reach = max(reach, i + nums[i])
    
    return True


def canJump2(nums: List[int]) -> bool:
    i, reach = 0, 0
    n = len(nums)
    
    while i <= reach and reach < n - 1:
        reach = max(reach, i + nums[i])
        i += 1

    return reach >= n - 1


def canJump3(nums: List[int]) -> bool:
    n = len(nums)
    last_index = n - 1

    for i in range(n - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i

    return last_index == 0


nums = [2,3,1,1,4]
print(canJump3(nums))


"""
canJump1 贪心算法-可以到达最远的位置：
    只需要获取当前位置 i 能跳到的最远位置是哪，在最远位置与 i 之间的所有位置它都可以跳跃到；
    只要最终得到的最远位置大于等于 len(nums) - 1, 就证明跳跃成功;
    时间复杂度: O(n); 空间复杂度: O(1);

canJump2:
    与 canJump1 原理相同，只是在代码实现上进行了优化，提前结束循环；
    时间复杂度: O(n); 空间复杂度: O(1);

canJump3 贪心算法-最早开始位置：
    如果想要跳跃到数组最后的位置，那么最早开始可以从哪里出发，如果最早开始位置可以到 0, 那么证明跳跃成功；
    时间复杂度: O(n); 空间复杂度: O(1);
"""