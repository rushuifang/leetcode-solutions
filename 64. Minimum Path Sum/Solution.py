class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            res = 0
            for row in grid:
                for el in row:
                    res += el
            return res
        for i in range(m - 1):
            grid[i + 1][0] += grid[i][0]
        for j in range(n - 1):
            grid[0][j + 1] += grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i - 1][j] < grid[i][j - 1]:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += grid[i][j - 1]
        print(grid)
        return grid[-1][-1]