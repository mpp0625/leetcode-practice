from typing import List


def numIslands1(grid: List[List[str]]) -> int:
    def dfs(grid, r, c):
        grid[r][c] = 0

        rows, cols = len(grid), len(grid[0])

        for i, j in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                dfs(grid, i, j)

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    num_lands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                num_lands += 1
                dfs(grid, r, c)

    return num_lands


def numIslands2(grid: List[List[str]]) -> int:
    from collections import deque

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    
    num_lands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                num_lands += 1
                grid[r][c] = "0"

                neighbors = deque([(r, c)])
                while neighbors:
                    r, c = neighbors.popleft()

                    for i, j in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                            grid[i][j] = "0"
                            neighbors.append((i, j))

    return num_lands


grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
print(numIslands2(grid))


"""
numIslands1 深度优先搜索：
    遍历矩阵，当遇到 1 时，则以其为起始节点开始进行深度优先搜索；
    在深度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。

    时间复杂度: O(m * n); 空间复杂度: O(m * n) 来源于递归调用栈，没调用一层就占用一帧栈空间，假设grid的元素全部为 `1`, 栈的深度将达到 m * n;


numIslands2 广度优先搜索:

"""