from typing import List


def searchMatrix1(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        for el in row:
            if el == target:
                return True
            
    return False


def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        curr = matrix[row][col]

        if curr == target:
            return True
        
        if curr > target:
            col -= 1
        else:
            row += 1

    return False


def searchMatrix3(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False

    n = len(matrix[0])

    for row in matrix:
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if row[m] == target:
                return True
            
            if row[m] > target:
                r = m - 1
            else:
                l = m + 1
    
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(searchMatrix2(matrix, target))


"""
searchMatrix1:
    时间复杂度：O(m * n)；空间复杂度：O(1)；

searchMatrix2 从右上角开始搜索（最快）:
    右上角的值：当前行最大，当前列最小；
    当前值 > target: 往左移动
    当前值 < target: 往下移动
    时间复杂度：O(m + n)；空间复杂度：O(1)；

searchMatrix3 每行使用二分查找：
    判断中间位置的值相对于 target 的大小；
    时间复杂度：O(mlog(n))；空间复杂度：O(1)；
"""