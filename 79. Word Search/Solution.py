class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(x, y, d):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[d]:
                return False
            if d == len(word) - 1:
                return True
            temp = board[x][y]
            board[x][y] = "0"
            found = dfs(x-1, y, d+1) or dfs(x+1, y, d+1) or dfs(x, y-1, d+1) or dfs(x, y+1, d+1)
            board[x][y] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
            