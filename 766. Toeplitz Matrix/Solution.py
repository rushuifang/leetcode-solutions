class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def dfs(i, j, num):
            if i >= m or j >= n:
                return True
            elif i < m and j < n and matrix[i][j] == num:
                return dfs(i + 1, j + 1, num)
            elif i < m and j < n and matrix[i][j] != num:    
                return False
        
        for i in range(m):
            num = matrix[i][0]
            if not dfs(i, 0, num):
                return False
        
        for j in range(n):
            num = matrix[0][j]
            if not dfs(0, j, num):
                return False
        return True


# Easier:
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True