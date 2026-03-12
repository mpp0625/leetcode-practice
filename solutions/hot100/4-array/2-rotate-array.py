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
    from math import gcd

    n = len(nums)
    m = gcd(n, k)

    for i in range(m):
        prev, cur = nums[i], i

        while True:
            cur = (cur + k) % n
            nums[cur], prev = prev, nums[cur]
            
            if cur == i:
                break

    print(nums)


def rotate3(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    count = 0

    for i in range(n):
        cur = i
        prev = nums[cur]

        while True:
            count += 1

            cur = (cur + k) % n
            nums[cur], prev = prev, nums[cur]

            if cur == i:
                break

        if count == n:
            break

    print(nums)


def rotate4(nums: List[int], k: int):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1

    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

    print(nums)


nums = [-1]
k = 2

print(rotate4(nums, k))


"""
rotate1 使用额外数组:
    时间复杂度: O(n)


rotate2 环状替换：
    这个方法在计算遍历次数时涉及到数学方面：
        假设从位置 0 开始，循环替换 nums 中的元素，当遍历再次回到位置 0 时，我们要解决的问题是如何确定遍历结束所有的元素全部完成替换；
        当再次回到位置 0 时，证明完成了 a 圈循环；在这个循环过程中完成了 b 个元素的替换，从而得到公式 a*n = b*k；
        由 an = bk 得出，an 是 k 的倍数也是 n 的倍数，所以 an 是 n 和 k 的公倍数；
        当第一次回到起始位置 0 时，说明本次遍历结束，所以 a 尽可能的小，取最小公倍数lcm(n, k); 可以得出当从起点出发，再次回到起点一共遍历了多少元素：lcm(n, k) / k;
        an = lcm(n, k)  -> b = lcm(n, k) / k  单次遍历的元素个数;
        总共遍历的次数 = n / b -> n / (lcm(n, k) / k) -> nk / lcm(n, k) 此公式是 n 和 k 最大公约数公式: gcd(a, b) = a * b / lcm(a, b)

    时间复杂度: O(n); 空间复杂度: O(1);

rotate3 环状替换 + 计数：
    上面的`环状替换`方法中关于最小公倍数的相对不易理解，所以在此方法中增加一个变量 `count` 用于计算已经有多少元素完成了变换；
    时间复杂度: O(n); 空间复杂度: O(1);

rotate4 翻转数组：
    将数组划分为两部分 [0 ~ n - k - 1] 位置的元素以及 [n - k ~ n - 1] 位置的元素;
    数组尾部的 [n - k ~ n - 1] 位置的元素（也就是 k 个）元素会移动到头部；
    数组头部的 [0 ~ n - k - 1] 位置的元素会移动到尾部；

    所以先将整个数组进行翻转，这样尾 -> 头，头 -> 尾；
    然后将 [0 ~ k - 1] 进行翻转；[k ~ n - 1] 进行翻转；
"""