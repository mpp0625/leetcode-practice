def getDigits(s: str, ptr: int):
    digits = ""

    while s[ptr].isdigit():
        digits += s[ptr]
        ptr += 1

    return digits, ptr


def getString(v: list):
    return "".join(v)


def decodeString(s: str) -> str:
    stk = []

    ptr = 0
    while ptr < len(s):
        cur = s[ptr]

        if cur.isdigit():
            digits, ptr = getDigits(s, ptr)
            stk.append(digits)

        elif cur.isalpha() or cur == "[":
            stk.append(cur)
            ptr += 1

        else:
            sub = []

            while stk[-1].isalpha():
                sub.append(stk.pop())

            stk.pop()  # "["
            stk.append(int(stk.pop()) * getString(sub[::-1]))

            ptr += 1

    return getString(stk)


s = "2[abc]3[cd]ef"
print(decodeString(s))


"""
decodeString 栈操作：
    如果当前字符是 `数字`, 那么就解析出一个数字（或多个数字，直到遇到非数字字符）并进栈；
    如果当前字符是 `字母` 或 `[`, 则进栈；
    如果当前字符是 `]`, 开始出栈：
        直到遇到的字符 `非字母(也就是 [)`, 按照出栈序列反转并转换成字符串；
        提取栈顶的数字(stack.pop()), 与上面的字符串拼接后重新入栈；
"""