from typing import List


def generate(numRows: int) -> List[List[int]]:
    ret = []

    for i in range(numRows):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[-1][j - 1] + ret[-1][j])

        ret.append(row)

    return ret


numRows = 5
print(generate(5))


"""
杨辉三角：
    在杨辉三角内部的任意元素（除边界以外），均是它所在位置左上方和右上方两个数的和。

generate 动态规划：
    每一行的第一个及最后一个元素为 1;
    其他元素的值为其上一行的 `左上` +  `右上`, C(n, i) = C(n - 1, i - 1) + C(n - 1, i);
"""