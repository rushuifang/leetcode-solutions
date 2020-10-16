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


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // col
            j = mid % col
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            elif matrix[i][j] < target:
                left = mid + 1
        return False