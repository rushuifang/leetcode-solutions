class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        storageR = []
        storageC = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i not in storageR:
                        storageR.append(i)
                    if j not in storageC:
                        storageC.append(j)
        for el in storageR:
            matrix[el] = [0] * c
        for el in storageC:
            for i in range(r):
                matrix[i][el] = 0
