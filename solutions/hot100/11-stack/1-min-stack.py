from typing import Union
import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = [math.inf]


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> Union[float, int]:
        return self.minStack[-1]


minStack = MinStack()

minStack.push(-2)
print(minStack.stack)

minStack.push(0)
print(minStack.stack)

minStack.push(-3)
print(minStack.stack)

print(minStack.getMin())

minStack.pop()
print(minStack.stack)

print(minStack.top())

print(minStack.getMin())


"""
空间复杂度：
    ‌数据栈 self.stack‌: 在最坏情况下，如果连续执行 n 次 push 操作，就会有 n 个元素依次被存入 self.stack 中，
    那么 self.stack 占用的空间随着元素个数的增加而线性增长，也就是占用 O(n) 的空间。
"""