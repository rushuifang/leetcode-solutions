class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                else:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.pop(0)
            d = matrix[i][j] + 1
            for ii, jj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= ii < m and 0 <= jj < n and matrix[ii][jj] > d:
                    matrix[ii][jj] = d
                    queue.append((ii, jj))
        return matrix
        