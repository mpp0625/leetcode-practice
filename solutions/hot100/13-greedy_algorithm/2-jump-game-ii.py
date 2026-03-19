from typing import List


def jump1(nums: List[int]) -> int:
    n = len(nums)
    maxPos, end, step = 0, 0, 0

    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])

            if i == end:
                end = maxPos
                step += 1

    return step if maxPos >= n - 1 else -1


def jump2(nums: List[int]) -> int:
    position = len(nums) - 1
    step = 0

    while position > 0:
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                step += 1
                break

    return step


nums = [1,2,1,1,1]  # [2,3,0,1,4], [1,2,1,1,1], [0], [1,2], [2,1,1,1,1], [2,3,1,1,0,4]
print(jump2(nums))


"""
jump1 正向查找可到达的最大位置：
    只有当前位置小于等于最大位置时，才需要更新，否则证明无法跳跃到终点；
    当跳跃到上一次跳跃达到的最大位置时，仍然没有到终点，则需要增加一次跳跃次数以及更新可到达的最大位置；

    maxPos: 当前位置最远可以跳跃到的位置；
    end: 每一次跳跃的终点位置；
    step: 跳跃的次数；

    时间复杂度: O(n); 空间复杂度: O(1);

jump2 反向查找出发位置：
    从后向前推每一次跳跃的落点位置，在一次跳跃的过程中可能有多个位置能够完成，保留距离当前落点最远的那个位置；
    时间复杂度: O(n²); 空间复杂度: O(1);
"""