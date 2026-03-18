from typing import List


def dailyTemperatures1(temperatures: List[int]) -> List[int]:
    if not temperatures:
        return []

    n = len(temperatures)

    if n == 1:
        return [0]

    stk = []

    for i in range(n):
        t = temperatures[i]

        for j in range(i + 1, n):
            if temperatures[j] > t:
                stk.append(j - i)
                break
        
        else:
            stk.append(0)

    return stk


def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    n = len(temperatures)

    stk = []
    ans = [0] * n

    for i in range(n):
        while stk and temperatures[i] > temperatures[stk[-1]]:
            prev_index = stk.pop()
            ans[prev_index] = i - prev_index

        stk.append(i)

    return ans


temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures2(temperatures))


"""
dailyTemperatures1 暴力法：
    时间复杂度: O(n²);

dailyTemperatures2 单调栈：
    stack 栈中记录还没有找到下一个更高温度的索引，没找到入栈，找到了出栈；
    时间复杂度: O(n);
"""