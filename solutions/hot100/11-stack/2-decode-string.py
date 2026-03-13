def decodeString(s: str) -> str:
    stack = []

    cur = ""
    ans = ""

    for c in s:
        if c.isdigit():
            if cur and not cur.isdigit():
                stack.append(cur)
                cur = ""
            cur += c

        elif c == "[":
            stack.append(int(cur))
            cur = ""

        elif c == "]":
            if cur:
                stack.append(int(cur))
            
            count = stack.pop()
            ans = cur * count + ans
            cur = ""
        else:
            cur += c

    print(stack)

    ans = ""
    while stack:
        s = stack.pop()
        c = stack.pop()

        ans = (s + ans) * c

    return ans


s = "3[a2[bc]]"
print(decodeString(s))