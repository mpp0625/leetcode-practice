from typing import List


def rotate1(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    dummy = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            row, col = i, j
            val = matrix[row][col]

            while not dummy[row][col]:
                dummy[row][col] = True

                row, col = col, n - 1 - row
                temp = matrix[row][col]

                matrix[row][col] = val

                val = temp

    print(matrix)


def rotate2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n -1 - j], matrix[j][n - 1 - i] = \
                matrix[n - 1 - j][i], matrix[n - 1 - i][n -1 - j], matrix[j][n - 1 - i], matrix[i][j]

    print(matrix)


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate2(matrix)


"""
rotate1 辅助的数组：
    用来标记当前矩阵中的元素是否已经是旋转后的；
    时间复杂度：O(n²)；空间复杂度：O(n²)；

rotate2 原地旋转：
    由于每次旋转实际移动 4 个位置的元素，可以把矩阵划分成元素数量相等的 4 块（如果 n 是基数，中心点独立出来）；
    只遍历左上角那一块的元素，每次位置变化都会引起其他 3 块的变化；
"""