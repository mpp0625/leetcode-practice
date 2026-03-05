from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])

    rows, cols = [False] * m, [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = cols[j] = True

    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0


"""
setZeroes 使用数组标记：
    时间复杂度：O(m * n)；空间复杂度：O(m + n)；
"""