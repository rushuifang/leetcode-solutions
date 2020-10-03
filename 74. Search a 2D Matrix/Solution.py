class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if len(matrix) == 1 and matrix[0] == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target > matrix[i][0] and i != m - 1:
                continue
            elif target < matrix[i][0]:
                return target in matrix[i - 1]
            elif i == m - 1:
                return target in matrix[m - 1]
            else:
                return True