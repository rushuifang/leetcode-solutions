class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral(r1, r2, c1, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        matrix = [[1] * n for _ in range(n)]
        l = [i for i in range(1, n ** 2 + 1)]
        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral(r1, r2, c1, c2):
                matrix[r][c] = l.pop(0)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return matrix
