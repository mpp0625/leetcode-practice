from typing import List


def searchMatrix1(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False

    cols = len(matrix[0])
    
    for row in matrix:
        l, r = 0, cols - 1

        if row[r] < target:
            continue

        if row[l] > target:
            return False

        while l <= r:
            m = (r - l) // 2 + l

            if row[m] == target:
                return True
            
            if row[m] > target:
                r = m - 1
            else:
                l = m + 1

    return False


def searchMatrix2(matrix: List[List[int]], target: int):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    s, e = 0, m * n - 1

    while s <= e:
        mid = (e - s) // 2 + s
        q, r = divmod(mid, n)

        if matrix[q][r] == target:
            return True
        
        if matrix[q][r] < target:
            s = mid + 1
        else:
            e = mid - 1

    return False


def searchMatrix3(matrix: List[List[int]], target: int):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    
    s, e = 0, m - 1
    while s < e:
        mid = (e - s + 1) // 2 + s

        if matrix[mid][0] == target:
            return True
        
        if matrix[mid][0] < target:
            s = mid
        else:
            e = mid - 1
        
    r = s

    s, e = 0, n - 1
    while s <= e:
        mid = (e - s) // 2 + s

        if matrix[r][mid] == target:
            return True
        
        if matrix[r][mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0

print(searchMatrix3(matrix, target))


"""
searchMatrix1 每行二分查找：
    时间复杂度: O(m * logn), 其中 m 为行数, n 为列数; m 遍历行, logn 二分查找行;
    空间复杂度: O(1);

searchMatrix2 仅一次二分查找：
    时间复杂度: O(logm * n);
    空间复杂度: O(1);

searchMatrix3 行列两次二分查找:
    先对`行`进行二分查找，此处需要注意的是：
        在计算 mid 时，采用的时`向上取整`的策略, mid = (e - s + 1) // 2 + s, `+ 1` 是一种向上取整的方式；

        当 `matrix[mid][0] > target` 时, 可以确定 mid 行大于 target, e = mid + 1;
        而 `matrix[mid][0] < target` 并不能确定 mid 行中的所有元素大于 target, 因为整行时升序的，所以 s = mid;

    时间复杂度: O(logm + logn);
    空间复杂度: O(1);
"""