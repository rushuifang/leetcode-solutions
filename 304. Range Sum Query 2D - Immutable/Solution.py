class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                ans += self.matrix[row][col]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Cache!
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not matrix or not matrix[0]:
            return
        r = len(matrix)
        c = len(matrix[0])
        self.dp = [[0 for _ in range(c + 1)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                self.dp[i][j + 1] = self.dp[i][j] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1, row2 + 1):
            ans += self.dp[row][col2 + 1] - self.dp[row][col1]
        return ans


# Better Cache!
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not matrix or not matrix[0]:
            return
        r = len(matrix)
        c = len(matrix[0])
        self.dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                self.dp[i + 1][j + 1] = (
                    self.dp[i + 1][j]
                    + self.dp[i][j + 1]
                    - self.dp[i][j]
                    + self.matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row2 + 1][col1]
            - self.dp[row1][col2 + 1]
            + self.dp[row1][col1]
        )
