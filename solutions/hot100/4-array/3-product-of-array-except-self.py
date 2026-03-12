from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)

    pre = 1
    for i in range(n):
        ans.append(pre)
        pre *= nums[i]

    suf = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suf
        suf *= nums[i]

    return ans


nums = [1,2,3,4]
print(productExceptSelf(nums))


"""
productExceptSelf1 左右乘积:
    遍历 [0 ~ n - 1] 先获得当前元素之前的所有元素乘积；
    再遍历 [n - 1 ~ 0] 将其值乘以当前元素之后的所有元素乘积；

    时间复杂度: O(n); 空间复杂度: O(1)（输出数组可以不算复杂度）; 
"""