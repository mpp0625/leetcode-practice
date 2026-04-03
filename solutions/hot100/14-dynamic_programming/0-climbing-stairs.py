def climbStairs(n: int) -> int:
    p, q, r = 0, 0, 1

    for _ in range(n):
        p = q
        q = r

        r = p + q

    return r


n = 4
print(climbStairs(n))


"""
climbStairs 动态规划：
    爬到第 x 级台阶的方案数为 f(x), 到达 x 级台阶可能是跨一级台阶也可能跨二级台阶，所以 f(x) = f(x - 1) + f(x - 2);
        从第 0 级开始爬，第 0 级可以看作只有 1 种方案；
        从第 0 级到第 1 级，只有 1 种方案；
        比如：
            f(0) = 1
            f(1) = 1
            f(2) = 2; 1,1 | 2; => f(0) + f(1);
            f(3) = 2; 1,1,1 | 1,2 | 2, 1; => f(1) + f(2)

    时间复杂度: O(n); 空间复杂度: O(1);
"""