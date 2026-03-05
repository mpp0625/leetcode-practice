from typing import List


def spiralOrder1(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    t = m * n

    dummy = [[False] * n for _ in range(m)]

    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    indice = 0

    res = []
    row, col = 0, 0

    while t:
        dummy[row][col] = True
        res.append(matrix[row][col])

        row_new, col_new = row + direction[indice][0], col + direction[indice][1]
        if not(0 <= row_new < m and 0 <= col_new < n and not dummy[row_new][col_new]):
            indice = (indice + 1) % len(direction)

        row, col = row + direction[indice][0], col + direction[indice][1]

        t -= 1

    return res


def spiralOrder2(matrix: List[List[int]]) -> List[int]:
    if not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    t, b, l, r = 0, m -1, 0, n - 1

    res = []

    while l <= r and t <= b:
        for i in range(l, r + 1):
            res.append(matrix[t][i])

        for j in range(t + 1, b + 1):
            res.append(matrix[j][r])
        
        if l < r and t < b:
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b][i])
            
            for j in range(b - 1, t, -1):
                res.append(matrix[j][l])

        t, b, l, r = t + 1, b - 1, l + 1, r - 1

    return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder2(matrix))


"""
spiralOrder1 模拟，完全按照螺旋走: 
    时间复杂度：O(m * n)；空间复杂度：O(m + n)

spiralOrder2 逐层模拟，有矩阵的最外层开始：
    上 top, left -> top, right
    右 top + 1, right -> bottom, right
    下 bottom, right -1 -> bottom, left
    左 bottom - 1, left -> top + 1, left

    上 -> 右 -> 下 -> 左 - > 上 ...

    时间复杂度：O(m * n)；空间复杂度：O(1)

"""