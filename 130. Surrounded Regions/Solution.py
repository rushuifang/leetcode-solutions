class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = "Seen"

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == "O":
                    dfs(ii, jj)

        for x in [0, m - 1]:
            for y in range(n):
                if board[x][y] == "O":
                    dfs(x, y)

        for x in range(m):
            for y in [0, n - 1]:
                if board[x][y] == "O":
                    dfs(x, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "Seen":
                    board[x][y] = "O"
