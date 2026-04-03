from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[: i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result


nums = [1,2,3]
print(permute(nums))

"""
第1层 backtrack([], [1,2,3])        ← 这里有一个 for 循环，i 可以是 0,1,2
  选1
  第2层 backtrack([1], [2,3])       ← 这里有一个 for 循环，i 可以是 0,1
    选2
    第3层 backtrack([1,2], [3])     ← 这里有一个 for 循环，i 只能是 0
      选3
      第4层 backtrack([1,2,3], []) 
        记录结果 ✅ return
      撤销3
      # 第3层的 for 循环：remaining=[3] 只有1个元素，i=0 是最后一个，循环结束
    return  ← 第3层结束，回到第2层
    撤销2
    # 第2层的 for 循环继续！remaining=[2,3]，i=0用过了，现在 i=1
    选3
    ...
"""