def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = list()

    for c in s:
        if c in pairs:
            if not stack or stack[-1] != pairs[c]:
                return False
            
            stack.pop()
        else:
            stack.append(c)
    
    return not stack


s = "(]"
print(isValid(s))


"""
注意：`([)]` 不是有效的，因为它的顺序错误的，应该按照`后遇到的括号先闭合`的顺序；
"""