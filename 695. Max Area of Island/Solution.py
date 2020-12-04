class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        
        def dfs(i, j):
            if grid[i][j] == 0 or grid[i][j] == 2:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 2
            area = 1
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                    area += dfs(ii, jj)
            return area
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans