class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        for row in range(m):
            for col in range(n):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if r >= 0 and r < m and c >= 0 and c < n:
                        if abs(board[r][c]) == 1:
                            live_neighbors += 1
                if (live_neighbors < 2 or live_neighbors > 3) and board[row][col] == 1:
                    board[row][col] = -1
                if live_neighbors == 3 and board[row][col] == 0:
                    board[row][col] = 2
            
        for row in range(m):
            for col in range(n):
                if board[row][col] <= 0:
                    board[row][col] = 0
                else:
                    board[row][col] = 1